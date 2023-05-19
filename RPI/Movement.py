'''
import numpy as np
import math
from megapi import *
from time import *
import socket
import pickle
import subprocess
import RPi.GPIO as GPIO

bot = MegaPi()
bot.start()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def set_wheel_speeds(front_left, front_right, rear_left, rear_right):
		# If neccessary multiply speeds by constants to get matching wheel speeds
    bot.motorRun(M2, int(rear_left))
    bot.motorRun(1, int(rear_right))
    bot.motorRun(2, -int(front_left))
    bot.motorRun(M1, -int(front_right))

def moveTo(prevPos, currentPos, nextPos):
	# Define the robot's movement capabilities
	MAX_SPEED = 200
	MIN_SPEED = 40

	# Calculate the distance in x and y
	dx = nextPos[0] - currentPos[0]
	dy = nextPos[1] - currentPos[1]
	distanceBetweenPoints = np.sqrt((dx)**2 + (dy)**2) #in cm

	# Determine the desired velocity vector based on the change in position
	vel_x = dx
	vel_y = -dy

	# Use inverse kinematics to calculate the wheel velocities
	front_left = (vel_x - vel_y)
	front_right = (vel_x + vel_y)
	rear_left = (vel_x + vel_y)
	rear_right = (vel_x - vel_y)

	# Scale the wheel velocities to the maximum speed
	scale_factor = MAX_SPEED / np.max(np.abs([front_left, front_right, rear_left, rear_right]))
	front_left *= scale_factor
	front_right *= scale_factor
	rear_left *= scale_factor
	rear_right *= scale_factor

	total_speed=totalSpeed(front_left, front_right, rear_left, rear_right, dx, dy)

	# Determine how much to deccel/accel based on angle to next point
	a=angleBetween(prevPos, currentPos, nextPos)
	steps=20

	# Create percentage array
	perc=np.linspace(MIN_SPEED/MAX_SPEED+a*0.15, 1, steps)

	# Accelerate up to Speed or halfway to next point,
	# whichever comes first
	delay=0
	dpos=0
	break_perc=999
	for p in perc[:-1]:
		set_wheel_speeds(front_left*p, front_right*p, rear_left*p, rear_right*p)
		sped=totalSpeed(front_left*p, front_right*p, rear_left*p, rear_right*p, dx, dy)
		dpos+=abs(sped*(delay+0.0205)) # Takes 0.041 seconds to set all 4 wheel speeds
		if dpos >= distanceBetweenPoints/2:
			break_perc=p
			break
		sleep(delay)

	# Set to full speed
	t = (distanceBetweenPoints-2*dpos)/total_speed # seconds
	if t > 0:
		set_wheel_speeds(front_left, front_right, rear_left, rear_right)
		sleep(t)

	# Slow down
	for p in reversed(perc[:-1]):
		if p > break_perc:
			continue
		set_wheel_speeds(front_left*p, front_right*p, rear_left*p, rear_right*p)
		sped=totalSpeed(front_left*p, front_right*p, rear_left*p, rear_right*p, dx, dy)
		dpos-=abs(sped*(delay+0.0205))
		if dpos <= 0:
			break
		sleep(delay)

def angleBetween(p1, p2, p3):
	try:
		v1 = (p1[0]-p2[0], p1[1]-p2[1])
		v2 = (p3[0]-p2[0], p3[1]-p2[1])
		dot = v1[0]*v2[0] + v1[1]*v2[1]

		mag1 = math.sqrt(v1[0]**2 + v1[1]**2)
		mag2 = math.sqrt(v2[0]**2 + v2[1]**2)

		if mag1 != 0 and mag2 != 0:
			return math.acos(round(dot/mag1/mag2, 2))/math.pi
		else:
			return 1
	except Exception as e:
		print(e)

# Calculates the total speed from the speed of each individual mecanum wheel speed
# Returns the total speed
def totalSpeed(front_left, front_right, rear_left, rear_right, dx, dy):
	radius = 3 # cm
	xspeed = (front_left+front_right+rear_left+rear_right)
	xspeed = xspeed/60*radius
	yspeed = (front_left-front_right-rear_left+rear_right)
	yspeed = yspeed/60*radius

	# Constant that accounts for the faster movement when
	# going forward and backwards
	if dx == 0:
		yspeed*=1.2
	else:
		angle=math.atan(abs(dy/dx))
		yspeed*=(1+angle/math.pi/2.5)

	return math.sqrt(xspeed**2 + yspeed**2)

# def getip():
#         cmd="ifconfig wlan0 | grep 'inet ' | awk '{print $2}'"
#         output = subprocess.check_output(cmd, shell=True).decode().strip()
#         return output
try:
	# Using Bluetooth Connection
	while True:
		mac='08:BE:AC:35:8A:B4'
		port=1
		points=[]
		with socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) as s:
			s.bind((mac, port))
			s.listen()
			print('waiting for connection')
			client, address = s.accept()
			print('connected by', address)
			data=b''
			while True:
				try:
					some = client.recv(4096)
					if not some:
							break
					data += some
				except Exception as e:
					break
			points=pickle.loads(data)
			client.close()
			s.close()

		print('press button to start')
		while True:
			if GPIO.input(18) == GPIO.HIGH:
				break
		print('starting print')
		sleep(1)
		# Plan the robot's movement
		for i, path in enumerate(points):
			for j in range(len(path)-1):
				# Pen Down
				if j < 1:
					moveTo(path[j], path[j], path[j+1])
				else:
					moveTo(path[j-1], path[j], path[j+1])
				#print('next coord')
			# Pen Up
			if i < len(points)-1 and points[i][-1] != points[i+1][0]:
				moveTo(points[i][-1], points[i+1][0])
			#print('next path')
		set_wheel_speeds(0,0,0,0)
		print('Print Complete')
except Exception as e:
	print(e)
	set_wheel_speeds(0,0,0,0)

# # Using IP connection
# try:
# 	while True:
# 		host=getip()
# 		print(host)
# 		port=6677
# 		points=[]
# 		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# 			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 			s.bind((host, port))
# 			s.listen()
# 			print('Waiting for connection...')
# 			conn, addr = s.accept()
# 			with conn:
# 				print('connected by', addr)
# 				data=b''
# 				while True:
# 					some = conn.recv(4096)
# 					if not some:
# 						break
# 					data += some

# 				points=pickle.loads(data)

# 				print('press button to start')
# 				while True:
# 					if GPIO.input(18) == GPIO.HIGH:
# 						break
# 				print('starting print')
# 				sleep(1)
# 				# Plan the robot's movement
# 				for i, path in enumerate(points):
# 					for j in range(len(path)-1):
# 						# Pen Down
# 						if j < 1:
# 							moveTo(path[j], path[j], path[j+1])
# 						else:
# 							moveTo(path[j-1], path[j], path[j+1])
# 						#print('next coord')
# 					# Pen Up
# 					if i < len(points)-1 and points[i][-1] != points[i+1][0]:
# 						moveTo(points[i][-1], points[i+1][0])
# 					#print('next path')
# 				set_wheel_speeds(0,0,0,0)
# except Exceptions as e:
# 	set_wheel_speed(0,0,0,0)
# 	print(e)

'''
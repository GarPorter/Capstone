from Backend.SvgToPoints import *
import socket
import pickle

# Sends array of points to RPI robot through IP host
# Param points: list
def sendToRPI(points):
    host = '192.168.0.192'
    port = 6677 # Same port as inputted on RPI
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print('connceted to RPI')
        data = pickle.dumps(points)
        s.sendall(data)
        print('sent data:', data[1:5])

# Remove duplicate from set but keep order
# Param seq: list
# Returns list
def oset(seq):
  seen = set()
  seen_add = seen.add
  return [x for x in seq if not (x in seen or seen_add(x))]

# Removes duplicates list from a list of lists
# Param list list_of_lists
# Returns list unique_lists
def rdl(list_of_lists):
  unique_lists = []
  for l in list_of_lists:
      if l not in unique_lists:
          unique_lists.append(l)
  return unique_lists

# Covers SVG file to array of points
# Param fileName: string
# Param param: extra parameter if needed to be sent from page
def getPoints(fileName, param=0):
    points=[]
    if 'Meander' in fileName:
        oldPoints = svg_to_points(fileName)[2:-6]
        for path in oldPoints:
            points.append(oset(path))
        # sendToRPI(points)
    elif 'Brownian' in fileName:
        oldPoints = svg_to_points(fileName)
        for path in oldPoints:
            if len(path) == param*2-2: # Correct path
                points.append(oset(path))
        # sendToRPI(points)
    elif 'Sierpinski' in fileName:
        oldPoints = svg_to_points(fileName)
        oldPoints=rdl(oldPoints)
        for path in oldPoints: # [0:14] for lower order
            path=[path[0], path[1], path[4], path[5]]
            points.append(path)
        # sendToRPI(points)
    elif 'Koch' in fileName:
        oldPoints = svg_to_points(fileName)[2:-5]
        oldPoints = oset(oldPoints[0])
        points=oldPoints[(len(oldPoints)+1)//2:]+oldPoints[:(len(oldPoints)+1)//2]
        points.append(points[0])
        # sendToRPI(points)
    elif 'Fib' in fileName:
        print('in fib')
        # sendToRPI(points)
    elif 'Lissajous' in fileName:
        points = svg_to_points(fileName)[2]
        points = oset(points)
        # sendToRPI(points)
    elif 'Voronoi' in fileName:
        print('got the points')
        # sendToRPI(points)

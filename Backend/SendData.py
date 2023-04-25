from Backend.SvgToPoints import *
import socket
import pickle
import subprocess

# Gets IP address of RPI from MAC address of RPI
# Returns IP address
def getIp():
    cmd = 'arp -a | findstr "b8-27-eb-75-0a-d5" '
    returned_output = subprocess.check_output((cmd),shell=True,stderr=subprocess.STDOUT)
    parse=str(returned_output).split(' ',1)
    ip=parse[1].split(' ')
    return ip[1]

# Sends array of points to RPI robot through IP host
# Param points: list
def sendToRPI(points):
    # host = getIp()
    host='192.168.0.205'
    print(host)
    port = 6677 # Same port as inputted on RPI
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print('connceted to RPI')
        data = pickle.dumps(points)
        s.sendall(data)

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

# Transforms points to start at origin and scale to set range
def transform(oldPoints):
    points=[]
    newPoints=[]
    maxmax=0
    scale=100
    xorigin, yorigin=oldPoints[0][0]
    for path in oldPoints:
        newPath=[]
        for coord in path:
            newPath.append(((coord[0]-xorigin), (coord[1]-yorigin)))
        points.append(newPath)
    maxmax = max([max(abs(coord[0]), abs(coord[1])) for path in points for coord in path if max(abs(coord[0]), abs(coord[1])) > maxmax])
    for path in points:
        newPath=[]
        for coord in path:
            newPath.append((round(coord[0]*scale/maxmax, 2), round(coord[1]*scale/maxmax, 2)))
        newPoints.append(newPath)
    return newPoints


# Covers SVG file to array of points
# Param fileName: string
# Param param: extra parameter if needed to be sent from page
def getPoints(fileName, param=0):
    points=[]
    if 'Meander' in fileName:
        oldPoints = svg_to_points(fileName)[2:-6]
        for path in oldPoints:
            points.append(oset(path))
        points=transform(points)
        sendToRPI(points)
    elif 'Brownian' in fileName:
        oldPoints = svg_to_points(fileName)
        for path in oldPoints:
            if len(path) == param*2-2: # Correct path; Param = Modb
                points.append(oset(path))
        points=transform(points)
        sendToRPI(points)
    elif 'Sierpinski' in fileName:
        oldPoints = svg_to_points(fileName)
        oldPoints=rdl(oldPoints)
        for path in oldPoints[0:14]: # [0:14] for lower order
            path=[path[0], path[1], path[4], path[5]]
            points.append(path)
        points=transform(points)
        sendToRPI(points)
    elif 'Koch' in fileName:
        oldPoints = svg_to_points(fileName)[2:-5]
        oldPoints = oset(oldPoints[0])
        points=oldPoints[(len(oldPoints)+1)//2:]+oldPoints[:(len(oldPoints)+1)//2]
        points.append(points[0])
        points=transform([points])
        sendToRPI(points)
    elif 'Fib' in fileName:
        points=transform([param])
        sendToRPI(points)
    elif 'Lissajous' in fileName:
        points = svg_to_points(fileName)[2]
        points = [oset(points)]
        points=transform(points)
        sendToRPI(points)
    elif 'Voronoi' in fileName:
        points=transform(param)
        sendToRPI(points)
    # elif 'Fern' in fileName:
    #     oldPoints = svg_to_points(fileName)
    #     for path in oldPoints:
    #         points.append(oset(path))
    #     return points


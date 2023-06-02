import socket
import pickle
import subprocess
from Backend.SvgToPoints import *

# def getIp():
#     """Gets the IP of the RPI based on the MAC address

#     Returns:
#         string: IP address
#     """
#     cmd = 'arp -a | findstr "B8-27-EB-8A-F5-2A" ' # Mac Address after findstr
#     returned_output = subprocess.check_output((cmd),shell=True,stderr=subprocess.STDOUT)
#     parse=str(returned_output).split(' ',1)
#     ip=parse[1].split(' ')
#     return ip[1]

def send_to_rpi(points):
    """Sends array of points to RPI robot through Bluetooth socket

    Args:
        points (2D list): the coordinates of points in the pattern
    """

    '''Using Bluetooth Connection'''
    mac="B8:27:EB:8A:F5:2A" # RPI 3B
    #mac="08:BE:AC:35:8A:B4" # RPI 2
    port = 2
    with socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) as s:
        s.connect((mac,port))
        print('connected to RPI')
        data=pickle.dumps(points)
        s.sendall(data)

    '''Using IP Connection'''
    # host=getIp()
    # print(host)
    # port = 6677 # Same port as inputted on RPI
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.connect((host, port))
    #     print('connceted to RPI')
    #     data = pickle.dumps(points)
    #     s.sendall(data)

def oset(seq):
    """Removes duplicates from a list but keeps the same order

    Args:
        seq (list): original list

    Returns:
        list: list without duplicates
    """
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def rdl(list_of_lists):
    """Removes duplicate lists from a 2D list

    Args:
        list_of_lists (2D list): original list

    Returns:
        2D list: updated 2D list without duplicate lists
    """
    unique_lists = []
    for l in list_of_lists:
        if l not in unique_lists:
            unique_lists.append(l)
    return unique_lists

def transform(oldPoints):
    """Transforms points to start at origin and scale to set domain

    Args:
        oldPoints (2D list): original points

    Returns:
        2D list: transformed points
    """
    points=[]
    newPoints=[]
    maxmax=0
    minmin=9999
    scale=10
    xorigin = min([coord[0] for path in oldPoints for coord in path if coord[0] < minmin])
    yorigin = min([coord[1] for path in oldPoints for coord in path if coord[1] < minmin])
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

def getPoints(fileName, param=0):
    """Distinguishes between patterns and sends appropriate points to RPI

    Args:
        fileName (string): the SVG file path of pattern
        param (int, optional): extra parameter if needed for some patterns. Defaults to 0.

    Returns:
        2D list: transformed points that are sent to RPI
    """
    points=[]
    if 'Meander' in fileName:
        oldPoints = svg_to_points(fileName)[2:-6]
        for path in oldPoints:
            points.append(oset(path))
        points=transform(points)[:-1]
        send_to_rpi(points)
        return points
    elif 'Brownian' in fileName:
        oldPoints = svg_to_points(fileName)
        for path in oldPoints:
            if len(path) == param*2-2: # Find Correct path; Param = Modb
                points.append(oset(path))
        points=transform(points)
        send_to_rpi(points)
        return points
    elif 'Sierpinski' in fileName:
        oldPoints = svg_to_points(fileName)
        oldPoints=rdl(oldPoints)
        for path in oldPoints[0:14]: # [0:14] to remove smallest triangles
            path=[path[0], path[1], path[4], path[5]]
            points.append(path)
        points=transform(points)
        send_to_rpi(points)
        return points
    elif 'Koch' in fileName:
        oldPoints = svg_to_points(fileName)[2:-5]
        oldPoints = oset(oldPoints[0])
        points=oldPoints[(len(oldPoints)+1)//2:]+oldPoints[:(len(oldPoints)+1)//2] # start at bottom rather than top
        points.append(points[0])
        points=transform([points])
        send_to_rpi(points)
        return points
    elif 'Fib' in fileName:
        points=transform([param])
        # send_to_rpi(points) # doesnt work correctly currently
        return points
    elif 'Lissajous' in fileName:
        points = svg_to_points(fileName)[2]
        points = [oset(points)]
        points=transform(points)
        send_to_rpi(points)
        return points
    elif 'Voronoi' in fileName:
        points=transform(param)
        send_to_rpi(points)
        return points
    elif 'Shapes' in fileName:
        points=transform(param)
        send_to_rpi(points)
    elif 'Chaos1' in fileName:
        points=transform(param)
        send_to_rpi(points)
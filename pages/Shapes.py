import streamlit as st
import matplotlib.pyplot as plt
from Backend.Shape_Dict import shape_options
import math
from Backend.SendData import getPoints

st.title('Simple Shapes')
st.write('''
This page offers a collection of simple geometric shapes, such as squares, circles,
 triangles, and more, which can be selected and sent to the robot for drawing.
By demonstrating the precise movements and agility of our robot with these basic shapes,
 users can witness its versatility and artistic capabilities. We can also demonstrate
   its ability to accurately follow a simple path and make precise turns. Overall,
   these simple shapes can help visualize the path planning and manueverability of
   the omni-directional robot.
''')

def gen_ellipse (radius_x, radius_y, num_points=50):
  coordinates = []
  angle = 0
  angle_increment = 2 * math.pi / num_points

  for _ in range(num_points):
    x = radius_x * math.cos(angle)
    y = radius_y * math.sin(angle)
    coordinates.append((x, y))
    angle += angle_increment

  return coordinates

fig, ax = plt.subplots()
ax.axis('off')
plt.xticks([])
plt.yticks([])
ax.set_aspect('equal')

shape = st.selectbox('Select a shape', [ 'Circle', 'Ellipse', 'Triangle', 'Rectangle', 'Hexagon', 'Star', 'Heart' ])
points=[]
if shape == 'Triangle':
  ax.set_aspect('auto')
if shape == 'Ellipse':
  x_radius = st.slider('x Radius', 1, 10, 5)
  y_radius = st.slider('y Radius', 1, 10, 2)
  points=[gen_ellipse(x_radius, y_radius)]
  points[0].append(points[0][0])
  plt.xlim(-12, 12)
  plt.ylim(-12, 12)

elif shape == 'Rectangle':
  w = st.slider('Width', 1, 10, 4)
  l = st.slider('Length', 1, 10, 3)
  points = [[(0,0), (l, 0), (l, -w), (0, -w), (0,0)]]
  plt.xlim(-1, 12)
  plt.ylim(-12, 1)
else:
  points = shape_options[shape]['points']

for path in points:
  x, y = zip(*path)
  ax.scatter(x, y)
  ax.plot(x, y)

c1, c2 = st.columns([9, 1])

with c1:
  st.write(fig)
with c2:
  ''
  ''
  ''
  if st.button('Print'):
    getPoints('Shapes', points)
    st.balloons()
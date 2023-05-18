import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from Backend.SendData import *

# Initialize x and y arrays to zero
if 'x' not in st.session_state or 'y' not in st.session_state:
  st.session_state.x = [0]
  st.session_state.y = [0]

x = st.session_state.x
y = st.session_state.y

st.title("The Chaos Game")
st.write('''The Chaos Game is a method of generating fractal patterns using a
 simple set of rules. It involves randomly selecting a point on a plane and then
 repeatedly applying a simple transformation to it, such as plotting another point
 at half the distance to a selected vertex in an equilateral triangle. The result
 is the Sierpinski Triangle.''')

st.header('Application')
st.write('''
 The Sierpinski triangle's unique self-similar properties make it a valuable tool
 in image compression. By using the triangle to represent an image as a set of triangles,
 the process can be lossless, scalable, and computationally efficient. Dividing the image
 into small blocks, each is compared to similar domain blocks until the best match
 is found and transformed recursively. This fractal compression technique enables
 the image to be stored and transferred more efficiently. The simplicity and
 versatility of the Sierpinski triangle make it an ideal tool for image compression.''')

st.header('Try it Yourself!')
st.write('_Note: The Printing start at Point C_')
st.write('Pick a random Vertex or skip forward 1000 steps')


a, b = 0, 0

col = st.columns([4, 6, 3, 3, 3, 6, 4])

# When 1000x is pressed choose random vertex and plot a point halfway to it
# Iterate 1000 times
with col[0]:
  if st.button('1000x'):
    for i in range(1000):
      r = np.random.rand()*3
      if r < 1:
        a, b = (-3-x[-1])/2 + x[-1], (0-y[-1])/2 + y[-1]
      elif r >= 1 and r < 2:
        a, b = (0-x[-1])/2 + x[-1], (3/np.sqrt(3)-y[-1])/2 + y[-1]
      else:
        a, b = (3-x[-1])/2 + x[-1], (0-y[-1])/2 + y[-1]
      x.append(a)
      y.append(b)

# When A is pressed plot a point halfway between A and previous point
with col[2]:
  if st.button('A'):
    a, b = (-3-x[-1])/2 + x[-1], (0-y[-1])/2 + y[-1]
    x.append(a)
    y.append(b)

# When B is pressed plot a point halfway between B and previous point
with col[3]:
  if st.button('B'):
    a, b = (0-x[-1])/2 + x[-1], (3/np.sqrt(3)-y[-1])/2 + y[-1]
    x.append(a)
    y.append(b)

# When C is pressed plot a point halfway between C and previous point
with col[4]:
  if st.button('C'):
    a, b = (3-x[-1])/2 + x[-1], (0-y[-1])/2 + y[-1]
    x.append(a)
    y.append(b)

# When Clear is pressed remove all points
with col[6]:
  if st.button('Clear'):
    st.session_state.x = [0]
    st.session_state.y = [0]
    x = [0]
    y = [0]

c1, c2 = st.columns([9, 1])
clicked=False
points=[]
# Column 2 holds the print button
with c2:
  ''
  ''
  ''
  if st.button('Print'):
    clicked=True
    points=getPoints('SVG/Sierpinski.svg')
    st.balloons()

if type(x) is not list or type(y) is not list:
  st.session_state.x = [0]
  st.session_state.y = [0]
  x = [0]
  y = [0]

plot = plt.figure(figsize=(8, 8))
plt.axis()
plt.text(-3.2, 0.05, 'A', fontsize=20)
plt.text(-0.3, 1.72, 'B', fontsize=20)
plt.text(2.95, 0.05, 'C', fontsize=20)
plt.plot((-3, 0, 3), (0, 3/np.sqrt(3), 0), 'bo')
plt.scatter(x, y, s=4)
plt.xticks([])
plt.yticks([])

# Column 1 holds the plot
with c1:
  st.write(plot)

if clicked:
  st.header('The Path being Printed')
  st.write('''Below are the points constituting the path being transmitted to the robot, starting from the red dot.
            The line(s) corresponds to the ideal pattern or path that should be followed to reproduce the desired drawing.
            However, due to the robot's linear interpolation between the points, there may be slight discrepancies
            between the exact pattern and the actual drawing. The individual paths are labeled below''')

  # Plot points
  fig, ax = plt.subplots()
  plt.xticks([])
  plt.yticks([])
  for i, path in enumerate(points):
      x, y = zip(*path)
      ax.plot(x, y)
      ax.scatter(x, y, s=25)
      ax.text(x[0]-0.15, (y[1]-y[0])/2+y[0], i+1, zorder=11)
      if i == 0:
        ax.scatter(x[0], y[0], c='red', zorder=10)
  ax.set_aspect('equal')
  st.pyplot(fig)

st.subheader('References')
st.write('''
- https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/iet-ipr.2019.0489
- https://www-users.york.ac.uk/~ss44/complex/compress.htm
''')
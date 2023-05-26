import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import random
from Backend.SendData import getPoints
from Backend.VoronoiBound import boundPoints

st.title("Voronoi Patterns")

st.write("""
Voronoi patterns are found all throughout nature, from the way bubbles interact to physical patterns found in giraffes, vegetables, mountain
range formations and more! We can use this for engineering applications through mapping and gps systems.

In a Voronoi pattern, every point within a given region is closer to the “seed” inside that region than it is
to any other point outside that region. Each point along a region's edge is equidistant from the two nearest seeds.
""")

st.header('Examples')
l, r = st.columns([5, 5])
with l:
  st.image('Images/voronoi_example.png', 'Spots on Giraffe')
with r:
  st.image('Images/voronoi2_example.jpg', 'Dragonfly Wings')
st.write("""
Try setting the amount of seeds to set up a map and see what happens!

_Notes: Dashed lines indicate infinitely long boundaries and will not be printed_
""")

# input
seedMax = 80
seeds = st.slider("Enter the seeds in your map", 4, seedMax, 17)
st.write("$s=$", seeds)

#put points onto the map
coordinates = []

for i in range(seeds):
    coordinates.append((random.uniform(0.0,0.5), random.uniform(0.0,0.5)))
pointsArr = np.array(coordinates)

#apply voronoi
from scipy.spatial import Voronoi, voronoi_plot_2d

vor = Voronoi(pointsArr)
fig = voronoi_plot_2d(vor)

c1, c2 = st.columns([9, 1])
clicked=False
plotpoints=[]
# Column containing button
with c2:
  ''
  ''
  ''
  if st.button('Print'):
    clicked = True
    vertices = st.session_state.vor.vertices
    lines = [st.session_state.vor.vertices[line] for line in st.session_state.vor.ridge_vertices if -1 not in line]

    points = boundPoints(lines)
    for ps in st.session_state.pointsArr:
      points.insert(0, [tuple(ps.tolist())])

    plotpoints=getPoints('SVG/Voronoi.svg', points)
    st.balloons()
  else:
    st.session_state.fig = fig
    st.session_state.pointsArr = pointsArr
    st.session_state.vor=vor

# Column containing plot.
# Dsiplays old plot if button is clicked otherwise creates new plot
with c1:
  if clicked:
    ax=st.session_state.fig.gca()
    ax.scatter(points[0][0][0], points[0][0][1], c='red')
    ax.text(points[0][0][0]-0.02, points[0][0][1]+0.01, 'Start', fontsize=12)
    st.write(st.session_state.fig)
  else:
    st.write(fig)

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
  for i, path in enumerate(plotpoints):
      x, y = zip(*path)
      ax.plot(x, y)
      ax.scatter(x, y, s=25)
      if i == 0:
        ax.scatter(x[0], y[0], c='red', zorder=10)
  ax.set_aspect('equal')
  st.pyplot(fig)

plt.close()

st.write("""
In this map, the seeds are represented by blue dots, the edges are outlined in black and the vertices are highlighted in orange.
""")

st.subheader('Image Sources')
st.write('''
- https://virtuosity.bentley.com/wp-content/uploads/2020/11/Voronoi-Diagram-GenerativeComponents-KB.png
- https://i.pinimg.com/originals/7f/03/b1/7f03b13acda415a024b481480f63e38e.jpg
''')
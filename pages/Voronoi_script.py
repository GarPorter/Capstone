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

plot = plt.figure()
c1, c2 = st.columns([9, 1])
clicked=False
points=[]
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

    getPoints('SVG/Voronoi.svg', points)
    st.balloons()
  else:
    st.session_state.fig = fig
    st.session_state.pointsArr = pointsArr
    st.session_state.vor=vor

# Column containing plot.
# Dsiplays old plot if button is clicked otherwise creates new plot
with c1:
  if clicked:
    st.write(st.session_state.fig)
  else:
    st.write(fig)

plt.close()

st.write("""
In this map, the seeds are represented by blue dots, the edges are outlined in black and the vertices are highlighted in orange.
""")
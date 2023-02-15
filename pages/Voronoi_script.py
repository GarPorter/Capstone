import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import random

st.title("Voronoi Patterns")

st.write("""
Voronoi patterns are found all throughout nature, from the way bubbles interact to physical patterns found in giraffes, vegetables, mountain 
range formations and more! We can use this for engineering applications through mapping and gps systems. 

In a Voronoi pattern, every point within a given region is closer to the “seed” inside that region than it is 
to any other point outside that region. Each point along a region's edge is equidistant from the two nearest seeds. 

Try setting the amount of seeds to set up a map and see what happens!
""")

# input
seedMax = 80
seeds = st.slider("Enter the seeds in your map", 1, seedMax, 17)
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

#plot results
figure, axes = plt.subplots()
plt.show()
plt.axis("off")
axes.set_aspect(1)
figure.tight_layout()

st.write(fig)

st.write("""
In this map, the seeds are represented by blue dots, the edges are outlined in black and the vertices are highlighted in orange.
""")
# Author: Dr. Xu Chen, University of Washington

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title('The Golden Spirals')
st.write('by: Xu Chen, University of Washington')
st.write("""
Plants evolved against perfect periodicity to maximize growth.
The Golden Ratio (1.61803...) is an irrational number that appears in Nature's growth patterns.
The seeds of sunflowers, leaves, branches and petals, for example, grow in spirals at the Golden Ratio.
Otherwise, growing new seeds and leaves at any simple fraction of angles, such as $\\frac{3}{4}\\pi$ and $\\frac{17}{20}\\pi$, will make lines that are stacked up, leading to either gaps between seeds or blocked sunshine and water for old leaves.
""")

st.write("Try reduce the graph density below and see what happens!")
st.write("Explore also the impact of the initial angle to the graph.")

r_rate = st.slider(
    'Enter a density parameter (smaller numbers yield denser graphs)', 0.001, 1.0, 0.01, 0.0001)
theta0 = st.slider("Enter a starting angle in degrees", 0, 360, 0)
# r_max = st.slider("Zoom factor", 1, 10, 1)
r_max = st.number_input("Zoom factor", 1, 10, 1)


# st.write("Density", r_rate)
# st.write("Starting angle", theta0)

Ntick = int(r_max/r_rate)
golden = (1 + 5 ** 0.5) / 2


# draw circle
figure, axes = plt.subplots()
draw_outer_circle = plt.Circle((0, 0), r_max, fill=False)

plt.axis("off")
axes.set_aspect(1)

# draw spirals

axes.set_xlim([-r_max, r_max])
axes.set_ylim([-r_max, r_max])

theta = theta0
r = r_rate
for ii in np.arange(1, Ntick):
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    theta = theta+golden
    r = r+r_rate
    axes.plot([x, r*np.cos(theta)], [y, r*np.sin(theta)], "k")

figure.tight_layout()

st.write(figure)

st.subheader('References')
st.write('''
- https://github.com/xchen-me/number-fun
''')
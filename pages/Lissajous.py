import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from Backend.Koch import *
from Backend.SendData import *
from Backend.SvgToPoints import *

st.title("Lissajous Curve")
st.write('Description')

Moda = st.slider("Pick Value for a", 1, 10, 3, key = "<one>")
Modb = st.slider("Pick Value for b", 1, 10, 3, key = "<two>")
t = np.linspace(-1, 1, num=100, endpoint=True)

x=np.sin(Moda*t)
y=np.sin(Modb*t)

figure, axes = plt.subplots()
plt.xticks([])
plt.yticks([])
axes.plot(x,y)

c1, c2 = st.columns([9, 1])
clicked=False
points=[]
with c2:
    ''
    ''
    ''
    if st.button('Print'):
        clicked=True
        figure.savefig('SVG/Lissajous.svg', format='svg', dpi=100)
        points=getPoints('SVG/Lissajous.svg')
        st.balloons()

with c1:
    if clicked:
        axes.scatter(x[0], y[0], c='red', zorder=100)
        axes.text(x[0]-0.08, y[0]-0.12, 'Start', fontsize=12, zorder=101)
    st.write(figure)

if clicked:
    st.header('The Path being Printed')
    st.write('''Below are the points constituting the path(s) being transmitted to the robot, starting from the red dot.
            The line(s) corresponds to the ideal pattern or path(s) that should be followed to reproduce the desired drawing.
            However, due to the robot's linear interpolation between the points, there may be slight discrepancies
            between the exact pattern and the actual drawing.''')
    # Plot points
    fig, ax = plt.subplots()
    plt.xticks([])
    plt.yticks([])
    for path in points:
        x, y = zip(*path)
        ax.plot(x, y)
        ax.scatter(x, y)
    ax.scatter(x[0], y[0], c='red', zorder=10)
    ax.set_aspect('equal')
    st.pyplot(fig)
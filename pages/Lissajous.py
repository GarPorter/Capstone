import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from Backend.Koch import *
from Backend.SendData import *
from Backend.SvgToPoints import *

st.title("Testing out Push to GitHub and Streamlit app")
st.write("Lissajous Curve")


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
with c2:
    ''
    ''
    ''
    if st.button('Print'):
        clicked=True
        figure.savefig('SVG/Lissajous.svg', format='svg', dpi=100)
        getPoints('SVG/Lissajous.svg')
        st.balloons()

with c1:
    if clicked:
        axes.scatter(x[0], y[0], c='red', zorder=100)
        axes.text(x[0]-0.08, y[0]-0.12, 'Start', fontsize=12, zorder=101)
    st.write(figure)
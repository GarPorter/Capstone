import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from Backend.Koch import *
from Backend.SendData import *

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

points=[]
c1, c2 = st.columns([9, 1])
with c1:
    st.write(figure)

with c2:
    ''
    ''
    ''
    if st.button('Print', key='lissajous'):
        figure.savefig('SVG/Lissajous.svg', format='svg', dpi=100)
        points = getPoints('SVG/Lissajous.svg')
        st.balloons()
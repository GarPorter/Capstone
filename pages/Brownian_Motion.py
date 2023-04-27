import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from Backend.SendData import *

st.header("Brownian Motion")
st.write('''Brownian motion aims to quantify the random motion of particles
            suspended in a medium. Utilizing Gaussian distribution we can track
            the motion of a particle through a medium''')


Modb = st.slider("Pick Value for b", 10, 100, 50, key = "<four>")

x=np.random.normal(0,5,Modb)
y=np.random.normal(0,5,Modb)

figure, axes = plt.subplots()
axes.plot(x,y)
plt.xticks([])
plt.yticks([])

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
    st.session_state.figure.savefig('SVG/Brownian.svg', format='svg', dpi=100)
    points=getPoints('SVG/Brownian.svg', Modb)
    st.balloons()
  else:
    st.session_state.figure = figure
    st.session_state.axes = axes
    st.session_state.x = x[0]
    st.session_state.y = y[0]

# Column containing plot.
# Dsiplays old plot if button is clicked otherwise creates new plot
with c1:
  if clicked:
    st.session_state.axes.scatter(st.session_state.x, st.session_state.y, c='red', zorder=100)
    st.session_state.axes.text(st.session_state.x-0.6, st.session_state.y+0.4, 'Start', fontsize=12, zorder=101)
    st.write(st.session_state.figure)
  else:
    st.write(figure)

plt.close()
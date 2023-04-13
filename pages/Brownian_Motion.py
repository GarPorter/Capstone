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

# Column containing button
with c2:
  ''
  ''
  ''
  if st.button('Print'):
    clicked = True
    st.session_state.figure.savefig('SVG/Brownian.svg', format='svg', dpi=100)
    getPoints('SVG/Brownian.svg', Modb)
    st.balloons()

# Column containing plot.
# Dsiplays old plot if button is clicked otherwise creates new plot
with c1:
  if clicked:
    st.write(st.session_state.figure)
  else:
    st.write(figure)

st.session_state.figure = figure
plt.close()
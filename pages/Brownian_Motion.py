import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.header("Brownian Motion")
st.write('''Brownian motion aims to quantify the random motion of particles
            suspended in a medium. Utilizing Gaussian distribution we can track 
            the motion of a particle through a medium''')


Modb = st.slider("Pick Value for b", 1, 10, 3, key = "<four>")

x=np.random.normal(0,1,Modb)
y=np.random.normal(0,1,Modb)

figure, axes = plt.subplots()
axes.plot(x,y)
st.write(figure)


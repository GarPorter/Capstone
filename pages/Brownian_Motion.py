import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.header("Brownian Motion")
st.write('''Brownian motion aims to quantify the random motion of particles
            suspended in a medium. Utilizing Gaussian distribution we can track 
            the motion of a particle through a medium''')

Modb = st.selectbox("How long would you like to walk?", ("Short", "Medium", "Long"))

if Modb == "Short":
    t=10
elif Modb == "Medium":
    t=50
elif Modb == "Long":
    t=100

x=np.random.normal(0,1,Modb)
y=np.random.normal(0,1,Modb)

figure, axes = plt.subplots()
axes.plot(x,y)
st.write(figure)


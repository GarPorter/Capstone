#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.title("Testing out Push to GitHub and Streamlit app")

st.write("Lissajous Curve")


Moda = st.slider("Pick Value for a", 1, 10, 3, key = "<one>")
Modb = st.slider("Pick Value for b", 1, 10, 3, key = "<two>")
t = np.linspace(0, 1, num=100, endpoint=True)

x=np.sin(Moda*t)
y=np.sin(Modb*t)

plt.plot(x,y)


# In[ ]:


st.title("Testing out Push to GitHub and Streamlit app")

st.write("Lissajous Curve")


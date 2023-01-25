#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from Koch import *

st.title("Testing out Push to GitHub and Streamlit app")

st.write("Lissajous Curve")


Moda = st.slider("Pick Value for a", 1, 10, 3, key = "<one>")
Modb = st.slider("Pick Value for b", 1, 10, 3, key = "<two>")
t = np.linspace(-1, 1, num=100, endpoint=True)

x=np.sin(Moda*t)
y=np.sin(Modb*t)

figure, axes = plt.subplots()
axes.plot(x,y)
st.write(figure)

''''''

st.header("Koch Snowflake")
st.write('koch snowflake')

ord = st.slider("Pick Order of Snowflake", 1, 8, 3, key = "<three>")

x, y = koch_snowflake(order=ord)

plot = plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.fill(x, y)
st.write(plot)


# In[ ]:





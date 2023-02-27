import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
# from Computations.Fibonacci import fibo
from Computations.Koch import *
# import multiprocessing as mp

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
st.write('''The Koch snowflake is a fractal shape that is formed by repeatedly
adding smaller equilateral triangles to the sides of an initial equilateral triangle.
 Each of these smaller triangles is then subjected to the same process, resulting in
 a shape that becomes increasingly complex and intricate with each iteration.
  The Koch snowflake is named after the Swedish mathematician Helge von Koch,
   who first described it in 1904.

The math behind the Koch snowflake involves a few key concepts, including self-similarity
 and infinite iteration. The snowflake is self-similar because each iteration produces
  a shape that is identical to the previous iteration, just scaled down. The infinite
   iteration means that the snowflake can be infinitely detailed, with an infinite perimeter
    but a finite area.''')

st.subheader('Application')
st.write('''
The Koch snowflake can be applied in the real world in a variety of ways, including
 in the design of coastlines, the development of antennas and other communication devices,
  and the creation of computer graphics and fractal art. It can also be used to explore
   concepts such as recursion, geometry, and topology in mathematics and computer science education.
    Additionally, the fractal nature of the snowflake has been used as a model for studying
     phenomena such as diffusion-limited aggregation and pattern formation in nature.''')

st.subheader('Try it Yourself!')
ord = st.slider("Pick Order of Snowflake", 1, 8, 3, key = "<three>")

x, y = koch_snowflake(order=ord)

plot = plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.fill(x, y)
st.write(plot)

''''''

# click = st.button('Paint')

# def genFibo(n):
#     nums = [1, 1]
#     n=n-2
#     while n > 0:
#         nums.append(nums[-1]+nums[-2])
#         n=n-1
#     return nums

# n = st.slider('Pick n Fibonacci Numbers', 2, 15, 9)

# fibo_nr = genFibo(n)  #Fibonacci numbers this could be calculated instead
# t = mp.Process(target=fibo, args=([fibo_nr]))

# if click:
#     t.start()

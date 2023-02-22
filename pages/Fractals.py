import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Creating art from fractals')
st.write('''
The Barnsley fern shows how graphically beautiful structures can be built from repetitive uses of mathematical formulas with computers.
In this demonstration, a fern is created by iterating a transformation of a point at a very high volume until you ultimatley end up
with a fern that replicates those found in nature.

Take a chance and try it out for yourself!
''')

colorUser = st.color_picker('Pick A Color for your fern', '#00f900')

def stem(x,y):
    return (0., 0.16*y)
def leaflets(x,y):
    return(0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)
def largeLeft(x,y):
    return(0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
def largeRight(x,y):
    return(-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)
functions = [stem, leaflets, largeLeft, largeRight]
st.write('How much transformations do you want your leaf to undergo?')
iterations = st.slider('Iterations?', 100, 100000, 50000)
x, y = 0, 0
x_list = []
y_list = []
for i in range(iterations):
    function = np.random.choice(functions, p=[0.02, 0.84, 0.07, 0.07])
    x, y = function(x, y)
    x_list.append(x)
    y_list.append(y)

plot = plt.figure(figsize=(8, 8))
plt.scatter(x_list, y_list, color = colorUser, s = 0.25)
st.write(plot)

st.write('''
For more information on the math involved and other applications of this phenomenon, visit https://en.wikipedia.org/wiki/Barnsley_fern
''')
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Creating art from fractals')
st.write('''
Fractals are found in nature...
''')

def stem(x,y):
    return (0., 0.16*y)
def leaflets(x,y):
    return(0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)
def largeLeft(x,y):
    return(0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
def largeRight(x,y):
    return(-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)
functions = [stem, leaflets, largeLeft, largeRight]

iterations = 50000
x, y = 0, 0
x_list = []
y_list = []
for i in range(iterations):
    function = np.random.choice(functions, p=[0.02, 0.84, 0.07, 0.07])
    x, y = function(x, y)
    x_list.append(x)
    y_list.append(y)

figure = plt.scatter(x_list,y_list, color = 'green')

st.pyplot(figure)
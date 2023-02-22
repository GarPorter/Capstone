import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import turtle

st.header("Fractal Tree")
st.write('''Trees are professionals at optimizing the surface area of their leaves to soak up sunlight''')

turt=turtle.Turtle()
turt.left(90)
turt.speed(0)

angle=st.slider('Branch Angle', 15, 45, 30)

def fractaltree(i):
    if i<5:
        return
    else:
        turt.forward(i)
        turt.left(angle)
        fractaltree(3*i/4)
        turt.right(angle*2)
        fractaltree(3*i/4)
        turt.left(angle)
        turt.back(i)
        
fractaltree(100)



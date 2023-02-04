import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

if 'x' and 'y' not in st.session_state:
  st.session_state['x'] = [0]
  st.session_state['y'] = [0]

x = st.session_state.x
y = st.session_state.y

st.header("The Chaos Game")
st.write('''The Chaos Game is a method of generating fractal patterns using a
 simple set of rules. It involves randomly selecting a point on a plane and then
 repeatedly applying a simple transformation to it, such as plotting another point
 at half the distance to a selected vertex in an equilateral triangle. The result
 is the Sierpinski Triangle. Try it yourself!''')
st.write('Pick a random Vertex or skip forward 1000 steps')

a, b = 0, 0

col = st.columns([4, 6, 3, 3, 3, 6, 4])

with col[0]:
  if st.button('1000x'):
    for i in range(1000):
      r = np.random.rand()*3
      if r < 1:
        a, b = (-3-x[-1])/2 + x[-1], (0-y[-1])/2 + y[-1]
      elif r >= 1 and r < 2:
        a, b = (0-x[-1])/2 + x[-1], (3/np.sqrt(3)-y[-1])/2 + y[-1]
      else:
        a, b = (3-x[-1])/2 + x[-1], (0-y[-1])/2 + y[-1]
      x.append(a)
      y.append(b)

with col[2]:
  if st.button('A'):
    a, b = (-3-x[-1])/2 + x[-1], (0-y[-1])/2 + y[-1]
    x.append(a)
    y.append(b)
with col[3]:
  if st.button('B'):
    a, b = (0-x[-1])/2 + x[-1], (3/np.sqrt(3)-y[-1])/2 + y[-1]
    x.append(a)
    y.append(b)
with col[4]:
  if st.button('C'):
    a, b = (3-x[-1])/2 + x[-1], (0-y[-1])/2 + y[-1]
    x.append(a)
    y.append(b)
with col[6]:
  if st.button('Clear'):
    st.session_state['x'] = [0]
    st.session_state['y'] = [0]
    x = [0]
    y = [0]

plot = plt.figure(figsize=(8, 8))
plt.axis()
plt.text(-3.2, 0.05, 'A', fontsize=20)
plt.text(-0.3, 1.72, 'B', fontsize=20)
plt.text(2.95, 0.05, 'C', fontsize=20)
plt.plot((-3, 0, 3), (0, 3/np.sqrt(3), 0), 'bo')
plt.scatter(x, y, s=4)
st.write(plot)
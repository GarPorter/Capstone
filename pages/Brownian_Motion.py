import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from Backend.SendData import *

st.title("Brownian Motion")
st.write('''Brownian motion aims to quantify the random motion of particles
            suspended in a medium. Utilizing Gaussian distribution we can track
            the motion of a particle through a medium''')

st.header('Examples')
l, r = st.columns([5, 5])
with l:
  st.image('Images/brownian_example.gif', 'The Motion of a Particle')
with r:
  st.image('Images/brownian2_example.gif', 'Brownian Animation')

st.write('''When a computer randomly generates numbers, they aren't exactly random.
            The computer looks at something called a Gaussian distribution in order
            to determine a number from a distribution of numbers. These random numbers
            can be changed by altering the Gaussian distribution.''')

modA = st.slider("Pick Value for range", 10, 100, 50, key = "<one>")

x1 = np.linspace(0,modA,100)
mean = np.mean(x1)
sd = np.std(x1)
gaussDist = (1/np.sqrt(2*np.pi*(sd**2))) * np.exp(-((x1-mean)**2)/(2*(sd**2)))

figure1, axes1 = plt.subplots()
axes1.plot(x1,gaussDist)
st.write(figure1)


st.write('''Now that we have a bit more understanding on what Gaussian distribution is
            Lets look at what happens when we plot two sets of random numbers.
            Imagine the red dot is a particle at the origin (0,0)
            What we see is a random data set where each point in the data set
            Is a random offset from the origin (0,0) (marked in red)
            The offset is always coming from the origin, not from the particals previous location''')


x=np.random.normal(0,5,modA)
y=np.random.normal(0,5,modA)
figure2, axes2 = plt.subplots()
axes2.plot(x,y)
axes2.plot(x,y)
axes2.plot(0,0, 'ro')
st.write(figure2)


st.write('''What if we want the particle to move in a random direction continuously, and not just from the origin?
            We can simply use the particles previous location and add the new random direction, causing the particle
            to take a 'step' in that direction.''')

def brownianMotion(modA):
    '''simulate and return an array of random "steps"
    according to brownian motion theory

    '''
    timeSteps = np.linspace(0, 10, modA)
    dt = timeSteps[1] - timeSteps[0]
    diffBrown = np.sqrt(dt) * np.random.normal(0, dt, modA-1)
    initialBrown = np.zeros(1)
    Brownian = np.concatenate((initialBrown, np.cumsum(diffBrown)))
    return np.array(Brownian)

figure3, axes3 = plt.subplots()
x2=brownianMotion(modA)
y2=brownianMotion(modA)
plt.plot(x2,y2)
plt.plot(x2[0],y2[0], 'ro')


c1, c2 = st.columns([9, 1])
clicked=False
points=[]
# Column containing button
with c2:
  ''
  ''
  ''
  if st.button('Print'):
    clicked = True
    st.session_state.figure3.savefig('SVG/Brownian.svg', format='svg', dpi=100)
    points = getPoints('SVG/Brownian.svg', modA)
    st.balloons()
  else:
    st.session_state.figure3 = figure3

# Column containing plot.
# Dsiplays old plot if button is clicked otherwise creates new plot
with c1:
  if clicked:
    st.write(st.session_state.figure3)
  else:
    st.write(figure3)

if clicked:
  st.header('The Path being Printed')
  st.write('''Below are the points constituting the path(s) being transmitted to the robot, starting from the red dot.
            The line(s) corresponds to the ideal pattern or path(s) that should be followed to reproduce the desired drawing.
            However, due to the robot's linear interpolation between the points, there may be slight discrepancies
            between the exact pattern and the actual drawing.''')
  # Plot points
  fig, ax = plt.subplots()
  plt.xticks([])
  plt.yticks([])
  for path in points:
      x, y = zip(*path)
      ax.plot(x, y)
      ax.scatter(x, y)
  ax.scatter(x[0], y[0], c='red', zorder=10)
  ax.set_aspect('equal')
  st.pyplot(fig)

plt.close()

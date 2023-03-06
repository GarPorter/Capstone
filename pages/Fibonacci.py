import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import time
from PIL import Image

st.header('Fibonacci Spiral')

st.write('''The Fibonacci spiral is a geometric pattern that occurs naturally in various
 aspects of the natural world, including the arrangement of leaves on a stem, the shape
   of shells and horns, and the branching of trees. It is named after the Italian mathematician
     Leonardo Fibonacci, who introduced the sequence of numbers that underpins it.

The math behind the Fibonacci spiral is based on the Fibonacci sequence, which is a series
 of numbers where each number is the sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8,
   13, 21, 34, 55, 89, 144, and so on. The sequence continues infinitely, with each new
     number being the sum of the two previous numbers.
''')
st.subheader('Application')
st.write('''The Fibonacci spiral can be used in wind turbine design to optimize the shape,
 length, and angle of the blades, which can improve the efficiency and performance of the
   turbine. By using the Fibonacci sequence and spiral, engineers can create blade shapes
     that have a gradual taper, reducing drag and improving energy capture. The length and
       angle of attack of the blades can also be determined using the Fibonacci sequence,
         resulting in a blade shape that is optimized for different wind speeds. Additionally,
           the Fibonacci spiral can be used to optimize the placement and orientation of wind
             turbines in a wind farm, maximizing the energy output while minimizing interference.''')


st.subheader('Try it Yourself!')
nums = st.slider('Number of Fibonacci Numbers', 2, 15, 5)

# Generates the first n Fibonacci numbers in an array
# Param: n (int) numbers to generate
# Returns: nums (array) array of fibonacci numbers
def genFibo(n):
  nums = [1, 1]
  n=n-2
  while n > 0:
      nums.append(nums[-1]+nums[-2])
      n=n-1
  return nums

# Fibonacci sequence, x, and y arrays
fa = genFibo(nums)[2:]
x = [-1, -4, -4, 1, -4, -25, -25, 9, -25, -169, -169, 64, -169]
y = [1, 0, -5, -5, 3, -5, -39, -39, 16, -39, -272, -272, 105]

# Create initial plot with margins, autoscaling, and first two squares
fig, ax = plt.subplots()
plt.xticks([])
plt.yticks([])
ax.axis('equal')
ax.margins(0.75, 0.75)
plt.autoscale()
ax.add_patch(Rectangle((-1,0), 1, 1, fc='None', ec='k'))
ax.add_patch(Rectangle((0,0), 1, 1, fc='None', ec='k'))

the_plot = st.pyplot(plt)

# Plots each square in the Fibonacci Spiral
# Param: i (int) index
# Param: x (array) array of x values
# Param: y (array) array of y values
def animate(i, x, y):
  plt.autoscale()
  ax.add_patch(Rectangle((x[i],y[i]), fa[i], fa[i], fc='None', ec='k'))
  the_plot.pyplot(plt)

# Adds delay to drawing of squares and calls animate function
for i in range(nums-2):
    time.sleep(0.5)
    animate(i, x, y)

# First two curves
Path = mpath.Path
pp1 = mpatches.PathPatch(
    Path([(-1, 1), (-1, 0), (0, 0)],
        [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", ec='r', transform=ax.transData)

ax.add_patch(pp1)
the_plot.pyplot(plt)

pp1 = mpatches.PathPatch(
    Path([(0, 0), (1, 0), (1, 1)],
        [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", ec='r', transform=ax.transData)

ax.add_patch(pp1)
the_plot.pyplot(plt)

p1 = (1, 1)

# Plotting curve
for i in range(len(fa)):
  time.sleep(0.25)
# alternate between - +, - -, + -, + +
  if i % 4 == 0:
    p2 = (p1[0]-fa[i], p1[1]+fa[i])
  elif i % 4 == 1:
    p2 = (p1[0]-fa[i], p1[1]-fa[i])
  elif i % 4 == 2:
    p2 = (p1[0]+fa[i], p1[1]-fa[i])
  else:
    p2 = (p1[0]+fa[i], p1[1]+fa[i])

  # for p3 alternate between (p1[0], p2[1]) and (p2[0], p1[1])
  # 1.03 makes the curves smoother
  if i % 2 == 0:
    p3 = (p1[0]/1.03, p2[1]/1.03)
  else:
    p3 = (p2[0]/1.03, p1[1]/1.03)

  pp1 = mpatches.PathPatch(
  Path([p1, p3, p2],
        [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
  fc="none", ec='r', transform=ax.transData)

  p1 = p2

  ax.add_patch(pp1)
  the_plot.pyplot(plt)

  # st.subheader('Examples')
  # img = Image.open('Images/Fibonacci_Spiral.png')
  # st.image(img, caption='Fibonacci Sprial of order 8')

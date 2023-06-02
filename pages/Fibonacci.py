import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import time
from PIL import Image
from Backend.SendData import getPoints

st.title('Fibonacci Spiral')

st.write('''The Fibonacci spiral is a geometric pattern that occurs naturally in various
 aspects of the natural world, including the arrangement of leaves on a stem, the shape
   of shells and horns, and the branching of trees. It is named after the Italian mathematician
     Leonardo Fibonacci, who introduced the sequence of numbers that underpins it.

The math behind the Fibonacci spiral is based on the Fibonacci sequence, which is a series
 of numbers where each number is the sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8,
   13, 21, 34, 55, 89, 144, and so on. The sequence continues infinitely, with each new
     number being the sum of the two previous numbers.
''')

st.header('Examples')
left, right = st.columns([5, 6])
with left:
    st.image(Image.open('Images/Pinecone_Fibonacci.jpg'), caption='Fibonacci in a Pinecone')
with right:
    st.image(Image.open('Images/Galaxy_Fibonacci.jpg'), caption='Fibonacci in a Spiral Galaxy')

st.header('Application')
st.write('''The Fibonacci spiral can be used in wind turbine design to optimize the shape,
 length, and angle of the blades, which can improve the efficiency and performance of the
   turbine. By using the Fibonacci sequence and spiral, engineers can create blade shapes
     that have a gradual taper, versus a parabolic, reducing drag and improving energy capture.
       The length and angle of attack of the blades can also be determined using the Fibonacci sequence,
         resulting in a blade shape that is optimized for different wind speeds.''')

col1, col2 = st.columns([9, 1.2])
with col1:
    st.header('Try it Yourself!')
with col2:
    toggle = st.select_slider('Animation?', ['No', 'Yes'])

nums = st.slider('Number of Fibonacci Numbers', 2, 15, 4)

def genFibo(n):
    """Generates the first n Fibonacci numbers in an array

    Args:
        n (int): number of fibonacci numbers to generate

    Returns:
        list: list of n fibonacci numbers
    """
    fib_nums = [1, 1]
    n=n-2
    while n > 0:
        fib_nums.append(fib_nums[-1]+fib_nums[-2])
        n=n-1
    return fib_nums

c1, c2 = st.columns([9, 1])
with c1:
    # Fibonacci sequence, x, and y arrays
    fa = genFibo(nums)[2:]
    x = [-1, -4, -4, 1, -4, -25, -25, 9, -25, -169, -169, 64, -169]
    y = [1, 0, -5, -5, 3, -5, -39, -39, 16, -39, -272, -272, 105]

    # Create initial plot with margins, autoscaling, and first two squares
    fig, ax = plt.subplots()
    if toggle == 'No':
        blocker = Rectangle((-1000, -1000), 2000, 2000, linewidth=1, edgecolor='white', facecolor='white', zorder=10)
        bl = ax.add_patch(blocker)

    plt.xticks([])
    plt.yticks([])
    ax.axis('equal')
    ax.margins(0.75, 0.75)
    plt.autoscale()
    ax.add_patch(Rectangle((-1,0), 1, 1, fc='None', ec='k'))
    ax.add_patch(Rectangle((0,0), 1, 1, fc='None', ec='k'))

    the_plot = st.pyplot(plt)

    # Adds delay to drawing of squares and calls animate function
    for i in range(nums-2):
        plt.autoscale()
        ax.add_patch(Rectangle((x[i],y[i]), fa[i], fa[i], fc='None', ec='k'))
        if toggle == 'Yes':
            time.sleep(0.5)
            the_plot.pyplot(plt)
    patches=[]

    # First two curves
    Path = mpath.Path
    pp1 = mpatches.PathPatch(
        Path([(-1, 1), (-1, 0), (0, 0)],[Path.MOVETO, Path.CURVE3, Path.CURVE3]),
        fc="none", ec='r', transform=ax.transData)

    pp2 = mpatches.PathPatch(
        Path([(0, 0), (1, 0), (1, 1)],
            [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
            fc="none", ec='r', transform=ax.transData)

    ax.add_patch(pp1)
    if toggle == 'Yes':
        the_plot.pyplot(plt)

    ax.add_patch(pp2)
    if toggle == 'Yes':
        the_plot.pyplot(plt)

    patches.append(pp1)
    patches.append(pp2)

    p1 = (1, 1)

    # Plotting curve
    for i in range(len(fa)):
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
        # (1.03 makes the spiral smoother)
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

        if toggle == 'Yes':
            time.sleep(0.25)
            the_plot.pyplot(plt)

        patches.append(pp1)

    plot_limits= [[(-1.6774891774891776, 1.6774891774891776), (-0.75, 1.75)], [(-2.5, 2.5),
          (-0.3629032258064515, 3.3629032258064515)], [(-6.532467532467533, 3.5324675324675328),
          (-2.25, 5.25)], [(-7.75, 4.75), (-5.657258064516129, 3.657258064516129)],
          [(-10.91991341991342, 15.91991341991342), (-11.0, 9.0)], [(-13.75, 18.75),
          (-6.608870967741934, 17.608870967741936)], [(-43.22727272727273, 27.227272727272727),
          (-20.75, 31.75)], [(-50.5, 34.5), (-43.16935483870968, 20.169354838709676)],
          [(-72.76190476190477, 111.76190476190477), (-80.25, 57.25)], [(-91.75, 130.75),
          (-49.89919354838709, 115.89919354838709)], [(-294.0584415584416, 189.05844155844156),
          (-147.0, 213.0)], [(-343.75, 238.75), (-300.5282258064516, 133.5282258064516)],
          [(-496.41341991341994, 768.41341991342), (-554.75, 387.75)], [(-626.5, 898.5),
          (-346.6854838709677, 789.6854838709677)]]

    # Static Plot
    if toggle == 'No':
        bl.remove()
        plt.xlim(plot_limits[nums-2][0][0], plot_limits[nums-2][0][1])
        plt.ylim(plot_limits[nums-2][1][0], plot_limits[nums-2][1][1])
        the_plot.pyplot(plt)

clicked=False
points=[]
with c2:
    ''
    ''
    ''
    # Convert matplotlib patches to array of points
    # if st.button('Print'):
    #   clicked=True
    #   points = []
    #   for patch in patches:
    #     vertices = patch.get_verts()
    #     for vertex in vertices[:-1]:
    #       points.append((round(vertex[0], 2), round(vertex[1], 2)))
    #   points=getPoints('Fib', points)
    #   st.balloons()

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

# Adds example and removes fade when reloading
st.markdown("<style>.element-container{opacity:1 !important}</style>", unsafe_allow_html=True)

st.subheader('More Examples')
st.image(Image.open('Images/Fibonacci_Spiral.png'), caption='Fibonacci Sprial of order 8')

lside, rside = st.columns([5, 5])
with lside:
    st.image(Image.open('Images/Hurricane_Fibonacci.jpg'), caption='Fibonacci in a Hurricane')

with rside:
    st.image(Image.open('Images/Seashell_Fibonacci.jpg'), caption='Fibonacci in a Seashell')

st.subheader("References")
st.write('- https://re.public.polimi.it/retrieve/33b5ac84-9ff6-4845-b0b2-cb2d3ae59f00/BLANJ02-22.pdf')
st.subheader("Image Sources")
st.write('''
- https://th-thumbnailer.cdn-si-edu.com/Eg1bVd-L4f5NiM0aNd4Hl5Q7M0M=/1072x720/filters:no_upscale():focal(1365x816:1366x817)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer/3a/70/3a70f58d-dabc-4d54-ba16-1d1548594720/2560px-fibonaccispiralsvg.jpg
- https://www.cnet.com/a/img/resize/94603a3913d0dde076277c20a9f528cc585b0e39/hub/2015/04/10/840be572-0ee4-46a9-b10a-7d1df1a83bf3/pattern01.jpg?auto=webp&width=1200
- https://www.cnet.com/a/img/resize/e2838d4492147bc9204c49f6cfb5d9a715f653d6/hub/2015/04/10/b729d545-6592-4477-a551-1c1ecb9d4ed7/pattern08.jpg?auto=webp&width=1200
- https://www.cnet.com/a/img/resize/2c392249ab7fcaae204386f83425a53b63f54985/hub/2015/04/10/d867ee14-43e0-4c69-b747-a24eeab8bd58/pattern03.jpg?auto=webp&width=1200
- https://www.cnet.com/a/img/resize/7deb04847abdd94ed7d7f572f979602dee6ad779/hub/2015/04/10/76c5fe02-b321-4615-b801-2479e80e432b/pattern02.jpg?auto=webp&width=1200
''')
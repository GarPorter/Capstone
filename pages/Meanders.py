import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.artist import Artist
from Backend.MeandersAlgo import *
from Backend.SendData import getPoints

st.title('Open Meander Curves')
st.write('''
Open meander curves are a type of curved pattern that is often used in electronic
circuits to create inductance, impedance, or a path for current flow. The open meander
curve consists of a series of alternating segments, each of which is a quarter or half-wavelength long,
depending on the desired frequency of operation. In this example, the curve intersects
a horizontal line n times and is self avoiding (ie. does not intersect itself).''')

st.header('Examples')
l, r = st.columns([5,5])
with l:
    st.image('Images/meander_example.jpg', 'Meandering River')
with r:
    st.image('Images/meander2_example.jpg', 'Hybrid Meander Structure')

st.header('Application')
st.write('''
The alternating segments of the open meander curve create a pattern that appears to
"meander" or zigzag back and forth along the length of the curve. This pattern
creates a distributed inductance and capacitance that affects the behavior of a
signal passing through the curve. They are are commonly used in radio frequency (RF)
circuits, particularly for creating filters, resonators, and other RF components.
They are compact and can be easily integrated into the layout of a circuit. Additionally,
the distributed inductance and capacitance of the meander line can be adjusted by
changing the size and shape of the segments, making it a highly customizable component.
''')

fig, ax = plt.subplots()
plt.xticks([])
plt.yticks([])
if 'start_text' not in st.session_state:
    st.session_state.start_text=ax.text(0, 0, 'start')

st.header('Try it Yourself!')
pt = st.slider("Number of Points", 2, 10, 3)

c1, c2 = st.columns([9, 1])
plot, firstx = createPlot(pt)
clicked=False
points=[]
# Column containing button
with c2:
    ''
    ''
    ''
    if st.button('Print'):
        clicked = True
        Artist.remove(st.session_state.start_text)
        st.session_state.plot.savefig('SVG/Meander.svg', format='svg', dpi=100)
        points=getPoints('SVG/Meander.svg')
        st.balloons()
    else:
        st.session_state.plot = plot
        st.session_state.firstx = firstx

# Column containing plot.
# Dsiplays old plot if button is clicked otherwise creates new plot
with c1:
    if clicked:
        ax2=st.session_state.plot.gca()
        st.session_state.start_text=ax2.text(st.session_state.firstx-0.4, 0.05, 'Start', fontsize=12)
        st.write(st.session_state.plot)
    else:
        st.write(plot)

if clicked:
    st.header('The Path being Printed')
    st.write('''Below are the points constituting the path being transmitted to the robot, starting from the red dot.
              The line(s) corresponds to the ideal pattern or path that should be followed to reproduce the desired drawing.
              However, due to the robot's linear interpolation between the points, there may be slight discrepancies
              between the exact pattern and the actual drawing.''')

    # Plot points
    for i, path in enumerate(points):
        x, y = zip(*path)
        ax.plot(x, y)
        ax.scatter(x, y, s=10)
        if i == 0:
            ax.scatter(x[0], y[0], c='red', zorder=10)
    st.pyplot(fig)

plt.close()

st.subheader('References')
st.write('''
- https://iopscience.iop.org/article/10.7567/JJAP.52.05DC08
- https://www.researchgate.net/figure/Parasitic-capacitances-in-meander-lines_fig8_224610758
- https://ieeexplore.ieee.org/document/6545045
''')

st.subheader('Image Sources')
st.write('''
- https://www.nps.gov/common/uploads/stories/images/nri/20161208/articles/C04A2B82-1DD8-B71B-0B670854A934F77D/C04A2B82-1DD8-B71B-0B670854A934F77D.jpg
- https://pub.mdpi-res.com/electronics/electronics-10-01583/article_deploy/html/images/electronics-10-01583-g003.png?1625111215
''')
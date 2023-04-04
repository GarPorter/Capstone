import streamlit as st
import matplotlib.pyplot as plt
from Backend.MeandersAlgo import *
from Backend.SendData import getPoints

st.title('Open Meander Curves')
st.write('''
Open meander curves are a type of curved pattern that is often used in electronic
circuits to create inductance, impedance, or a path for current flow. The open meander
curve consists of a series of alternating segments, each of which is a quarter or half-wavelength long,
depending on the desired frequency of operation. In this example, the curve intersects
a horizontal line n times and is self avoiding (ie. does not intersect itself).''')

st.subheader('Application')
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

st.subheader('Try it Yourself!')
pt = st.slider("Number of Points", 2, 10, 3)

c1, c2 = st.columns([9, 1])
plot = createPlot(pt)
clicked=False
# Column containing button
with c2:
  ''
  ''
  ''
  if st.button('Print'):
    clicked = True
    st.session_state.plot.savefig('SVG/Meander.svg', format='svg', dpi=100)
#     st.image('SVG/Meander.svg')
    getPoints('SVG/Meander.svg')

# Column containing plot.
# Dsiplays old plot if button is clicked otherwise creates new plot
with c1:
  if clicked:
    st.write(st.session_state.plot)
  else:
    st.write(plot)

st.session_state.plot = plot

plt.close()

st.subheader('References')
st.write('''
- https://iopscience.iop.org/article/10.7567/JJAP.52.05DC08
- https://www.researchgate.net/figure/Parasitic-capacitances-in-meander-lines_fig8_224610758
- https://ieeexplore.ieee.org/document/6545045
''')

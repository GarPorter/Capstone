import streamlit as st
from Computations.MeandersAlgo import *

st.title('Open Meander Curves')
st.write('''
Open meander curves are a type of curved pattern that is often used in electronic
circuits to create inductance, impedance, or a path for current flow. The open meander
curve consists of a series of alternating segments, each of which is a quarter or half-wavelength long,
depending on the desired frequency of operation. In this example, the curve intersects
a horizontal line n times and is self avoiding (ie. does not intersect itself).

The alternating segments of the open meander curve create a pattern that appears to
"meander" or zigzag back and forth along the length of the curve. This pattern
creates a distributed inductance and capacitance that affects the behavior of a
signal passing through the curve. They are are commonly used in radio frequency (RF)
circuits, particularly for creating filters, resonators, and other RF components.
They are compact and can be easily integrated into the layout of a circuit. Additionally,
the distributed inductance and capacitance of the open meander curve can be adjusted by
changing the size and shape of the segments, making it a highly customizable component.
''')

pt = st.slider("Number of Points", 1, 12, 3)

plot = createPlot(pt)

st.write(plot)

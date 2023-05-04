import streamlit as st
import matplotlib.pyplot as plt
from Backend.Koch import *
from Backend.SendData import *

st.header("Koch Snowflake")
st.write('''The Koch snowflake is a fractal shape that is formed by repeatedly
adding smaller equilateral triangles to the sides of an initial equilateral triangle.
 Each of these smaller triangles is then subjected to the same process, resulting in
 a shape that becomes increasingly complex and intricate with each iteration.
  The Koch snowflake is named after the Swedish mathematician Helge von Koch,
   who first described it in 1904.

The math behind the Koch snowflake involves a few key concepts, including self-similarity
 and infinite iteration. The snowflake is self-similar because each iteration produces
  a shape that is identical to the previous iteration, just scaled down. The infinite
   iteration means that the snowflake can be infinitely detailed, with an infinite perimeter
    but a finite area.''')

st.subheader('Application')
st.write('''
The Koch snowflake can be applied in the real world in a variety of ways, including
 in the design of coastlines, the development of antennas and other communication devices,
  and the creation of computer graphics and fractal art. It can also be used to explore
   concepts such as recursion, geometry, and topology in mathematics and computer science education.
    Additionally, the fractal nature of the snowflake has been used as a model for studying
     phenomena such as diffusion-limited aggregation and pattern formation in nature.''')

st.subheader('Try it Yourself!')
st.write('_Note: Printing is only available up to order 4_')
ord = st.slider("Pick Order of Snowflake", 1, 8, 3, key = "<three>")

x, y = koch_snowflake(order=ord)

plot = plt.figure(figsize=(8, 8))
plt.xticks([])
plt.yticks([])
plt.axis('equal')
plt.fill(x, y)

clicked=False
c1, c2 = st.columns([9, 1])
if ord < 5:
    with c2:
        ''
        ''
        ''
        if st.button('Print'):
            clicked=True
            plot.savefig('SVG/Koch.svg', format='svg', dpi=100)
            getPoints('SVG/Koch.svg')
            st.balloons()

with c1:
    if clicked:
        plt.scatter(0, -5.75, c='red', zorder=100)
        plt.text(-0.5, -6.2, 'Start', fontsize=15, zorder=101)
    st.write(plot)

st.subheader('References')
st.write('''
- https://en.wikipedia.org/wiki/Koch_snowflake
- https://www.nointrigue.com/docs/notes/uni/tspwater/mytalk.pdf
- https://sites.google.com/a/maret.org/advanced-math-7-final-project-2014/architecture-and-arts/fractals-koch-snowflake
- https://www.ijert.org/research/analysis-of-koch-snowflake-fractal-antenna-for-multiband-application-IJERTV3IS041857.pdf
''')
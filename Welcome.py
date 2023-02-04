import streamlit as st

st.set_page_config(page_title='Welcome')

st.title('Welcome to our Capstone Project')
st.write('''The world is interconnected with complex feedback. Engineered systems, however, usually work on a
fixed time index. Leveraging 3D printing, number theory, and control engineering, this project will
design, build, and demonstrate a robotic drawing machine that exploits the power of feedback from
asynchronous data. Classic sensor fusion has established the foundation to estimate system states at
the probabilistic optimum. Emerging compressive sensing and multichannel computation are ideal for
interacting with high-dimensional spatial data via randomization-based decoding, but have been
disconnected from temporal dynamic data in realtime control systems. The heterogeneous sensing and
control exploited in this project will not only faithfully capture intricate dynamics with dissected and
asynchronous observations, but also enable agile closed-loop operations under realtime computation
constraints.''')
st.header('Team')
st.write('Boris Popov | Garrett Porter | Alejandro Martin-Villa')

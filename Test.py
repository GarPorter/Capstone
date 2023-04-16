import streamlit as st
from st_pages import Page, show_pages

# Specify what pages should be shown in the sidebar, and what their titles
# and icons should be

# Icons Link - https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

show_pages(
    [
        Page("Test.py", "Welcome", ":house:"),
        Page("pages/Lissajous.py", "Lissajous", ":curly_loop:"),
        Page("pages/Koch_Snowflake.py", "Koch Snowflake", ":snowflake:"),
        Page("pages/The_Chaos_Game.py", "Chaos Game", ":space_invader:"),
        Page("pages/Brownian_Motion.py", "Brownian", ":floppy_disk:"),
        Page("pages/Voronoi_script.py", "Voronoi", ":world_map:"),
        Page("pages/Meanders.py", "Meanders", ":desert_island:"),
        Page("pages/Fractals.py", "Fractals", ":herb:"),
        Page("pages/Tree.py", "Tree", ":maple_leaf:"),
        Page("pages/Chaos.py", "Chaos", ":milky_way:"),
        Page("pages/Fibonacci.py", "Fibonacci", ":sunflower:")
    ]
)


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

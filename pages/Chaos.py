import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Source - https://www.dynamicmath.xyz/strange-attractors/

# Current Issues:
#       1.) The equation parameters (ie. alpha) can't be updated to the figure --> Nothing happens when moving the slider
#       2.) Rucklidge equation isn't plotting, probably because the time step is too big or way too small
#       3.) The Plot title is wrong (all titled Lorenz), need to update the respective titles later
#       4.) The amount of options user has is overwhelming, maybe fix time step and number of steps to make it easier

# Lorenz attractor function
def lorenz_attractor(x, y, z, sigma=10., beta=2.67, rho=28.):
    x_dot = sigma * (y - x)
    y_dot = x * (rho - z) - y
    z_dot = x * y - beta * z
    return x_dot, y_dot, z_dot

# Rossler attractor function
def rossler_attractor(x, y, z, a=0.1, b=0.1, c=14.):
    x_dot = -y - z
    y_dot = x + a*y
    z_dot = b + z*(x-c)
    return x_dot, y_dot, z_dot

# Rössler attractor function
def rucklidge_attractor(x, y, z, alpha=0.2, beta=9.0, gamma=0.7):
    x_dot = y - z
    y_dot = z - x*alpha
    z_dot = beta + x*y - gamma*z
    return x_dot, y_dot, z_dot

# Thomas attractor function
def thomas_attractor(x,y,z, b=0.208186):
    x_dot = np.sin(y) - b*x
    y_dot = np.sin(z) - b*y
    z_dot = np.sin(x) - b*z
    return x_dot, y_dot, z_dot

# Aizawa attractor function
def aizawa_attractor(x,y,z,a=0.95,b=0.7,c=0.6,d=3.5,e=0.25,f=0.1):
    x_dot = (z-b)*x - d*y
    y_dot = x*d + (z-b)*y
    z_dot = c + a*z - (z*z*z)/3 - (x*x + y*y)*(1 + e*z) + f*z*(x*x*x)
    return x_dot, y_dot, z_dot


#def _attractor(x,y,z):
#    x_dot = 
#    y_dot = 
#    z_dot = 
#    return x_dot, y_dot, z_dot

# Computes results
def simulate_chaos(attractor_function, steps=10000, dt=0.01):
    xs = np.empty(steps + 1)
    ys = np.empty(steps + 1)
    zs = np.empty(steps + 1)

    xs[0], ys[0], zs[0] = (0., 1., 1.05)

    for i in range(steps):
        x_dot, y_dot, z_dot = attractor_function(xs[i], ys[i], zs[i])
        xs[i+1] = xs[i] + (x_dot * dt)
        ys[i+1] = ys[i] + (y_dot * dt)
        zs[i+1] = zs[i] + (z_dot * dt)

    return xs, ys, zs

# Streamlit app
st.title("Chaos Equation Demonstrations")
st.write('''Chaos equation attractors are mathematical constructs that describe the 
        behavior of chaotic systems. Chaotic systems are systems that exhibit seemingly 
        random behavior, but which actually follow deterministic rules. These attractors 
        can be used to describe the behavior of many natural systems, including weather 
        patterns, fluid flow, and the behavior of populations in ecological systems.
        
        An attractor is a set of states in a dynamical system to which the system evolves 
        over time, regardless of its starting point. It is a mathematical concept used 
        to describe the long-term behavior of a system. Attractors can be stable, meaning 
        that the system will eventually converge to a fixed point or limit cycle, or 
        they can be chaotic, meaning that the system will exhibit sensitive dependence 
        on initial conditions and will never converge to a fixed point.

        There are many systems that exhibit chaotic traits. Check out the following systems
        and change the parameters to see the behaviour of the solution curves. 
        
        To witness the motion that the sytems behave in, create your designs and hit print for a special 
        robotic demonstration.
        ''')


# Dropdown menu to select the attractor
attractor = st.selectbox(
    "Select an attractor:",
    ("Lorenz", "Rossler", "Rucklidge", "Thomas", "Aizawa")
)

# Set default parameters for each attractor
if attractor == "Lorenz":
    sigma = st.slider("Sigma", min_value=0.1, max_value=200., value=10., step=0.01)
    beta = st.slider("Beta", min_value=0.1, max_value=200., value=2.67, step=0.01)
    rho = st.slider("Rho", min_value=0.1, max_value=200., value=28., step=0.01)
    attractor_function = lorenz_attractor
elif attractor == "Rossler (Out of Order)":
    a = st.slider("a", min_value=0.01, max_value=0.5, value=0.1, step=0.01)
    b = st.slider("b", min_value=0.01, max_value=0.5, value=0.1, step=0.01)
    c = st.slider("c", min_value=5., max_value=20., value=14., step=0.1)
    attractor_function = rossler_attractor
elif attractor == "Rucklidge":
    alpha = st.slider("alpha", min_value=0.01, max_value=0.5, value=0.2, step=0.01)
    beta = st.slider("beta", min_value=0.01, max_value=15., value=9.0, step=0.01)
    gamma = st.slider("gamma", min_value=0.01, max_value=2., value=0.7, step=0.1)
    attractor_function = rucklidge_attractor
elif attractor == "Thomas":
    b = st.slider("b", min_value=0.01, max_value=0.5, value=0.208186, step=0.01)
    attractor_function = thomas_attractor
elif attractor == "Aizawa":
    a = st.slider("a", min_value=0.01, max_value=1.5, value=0.95, step=0.01)
    b = st.slider("b", min_value=0.01, max_value=1.5, value=0.7, step=0.01)
    c = st.slider("c", min_value=0.01, max_value=1.5, value=0.6, step=0.01)
    d = st.slider("d", min_value=0.01, max_value=5.0, value=3.5, step=0.01)
    e = st.slider("e", min_value=0.01, max_value=0.5, value=0.25, step=0.01)
    f = st.slider("f", min_value=0.01, max_value=0.5, value=0.1, step=0.01)
    attractor_function = aizawa_attractor

# set up the resolution and step size
steps = st.slider("Number of Steps", min_value=1000, max_value=40000, value=10000, step=1000)
dt = st.slider("Time Step (dt)", min_value=0.001, max_value=0.03, value=0.01, step=0.001)

# Gain the appropiate results
xs, ys, zs = simulate_chaos(attractor_function, steps, dt)

# Plot the results
fig, ax = plt.subplots(figsize=(10,10))
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Lorenz Attractor")

ax.plot(xs, ys, lw=0.5, color='purple')
plt.show()

st.pyplot(fig)





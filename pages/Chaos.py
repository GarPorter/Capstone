import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from Backend.SendData import getPoints

# Source - https://www.dynamicmath.xyz/strange-attractors/

# Current Issues:
#       1.) The equation parameters (ie. alpha) can't be updated to the figure --> Nothing happens when moving the slider
#       2.) Rucklidge equation isn't plotting, probably because the time step is too big or way too small
#       3.) The Plot title is wrong (all titled Lorenz), need to update the respective titles later
#       4.) The amount of options user has is overwhelming, maybe fix time step and number of steps to make it easier
#       5.) Printing currently is not doing it right

# Aizawa attractor function
# needs scale of 10
def aizawa_attractor(x,y,z,a=0.95,b=0.7,c=0.6,d=3.5,e=0.25,f=0.1):
    x_dot = (z-b)*x - d*y
    y_dot = x*d + (z-b)*y
    z_dot = c + a*z - (z*z*z)/3 - (x*x + y*y)*(1 + e*z) + f*z*(x*x*x)
    return x_dot, y_dot, z_dot

# needs scale of 1/2
def lorenz_attractor(x, y, z, sigma=10., beta=2.67, rho=28.):
    x_dot = sigma * (y - x)
    y_dot = x * (rho - z) - y
    z_dot = x * y - beta * z
    return x_dot, y_dot, z_dot

def rossler_attractor(x, y, z, a=0.1, b=0.1, c=14.):
    x_dot = -y - z
    y_dot = x + a*y
    z_dot = b + z*(x-c)
    return x_dot, y_dot, z_dot

# Thomas attractor function
def thomas_attractor(x,y,z, b=0.208186):
    x_dot = np.sin(y) - b*x
    y_dot = np.sin(z) - b*y
    z_dot = np.sin(x) - b*z
    return x_dot, y_dot, z_dot

#prefers to have the z axis displayed
def three_scroll(x,y,z, a=32.48, b=45.84, c=1.18, d=0.13, e=0.57, f=14.7):
    x_dot = a * (y - x) + d * x * z
    y_dot = b * x - (x * z) + f * y
    z_dot = c * z + x * y - e * x * x
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
        behavior of chaotic systems. Attractors can be stable, meaning
        that the system will eventually converge to a fixed point or limit cycle, or
        they can be chaotic, meaning that the system will exhibit sensitive dependence
        on initial conditions and will never converge to a fixed point.Chaotic systems
        are systems that exhibit seemingly random behavior, but which actually follow
        deterministic rules. These attractors can be used to describe the behavior of
        many natural systems, including weather patterns, fluid flow, and the behavior
        of populations in ecological systems.''')

st.subheader("Try it Yourself!")
st.write('''There are many systems that exhibit chaotic traits. Check out the following systems
        and change the parameters to see the behaviour of the solution curves.''')

st.write('''To witness the motion that the sytems behave in, create your designs and hit print for a special
        robotic demonstration! Note that the actual systems are in 3D but they are being plotted in 2D by the
        X and Y axis.''')

# Dropdown menu to select the attractor
attractor = st.selectbox(
    "Select an attractor:",
    ("Lorenz", "Thomas", "Aizawa") #Rossler and Rucklidge out of order atm
)

# Set default parameters for each attractor
if attractor == "Lorenz":
    attractor_function = lorenz_attractor
elif attractor == "Rossler (Out of Order)":
    attractor_function = rossler_attractor
elif attractor == "Rucklidge":
    attractor_function = three_scroll
elif attractor == "Thomas":
    attractor_function = thomas_attractor
elif attractor == "Aizawa":
    attractor_function = aizawa_attractor

# set up the resolution and step size
steps = st.slider("Number of Steps", min_value=1000, max_value=40000, value=10000, step=1000)
dt = st.slider("Time Step (dt)", min_value=0.001, max_value=0.03, value=0.01, step=0.001)

# Gain the appropiate results
xs, ys, zs = simulate_chaos(attractor_function, steps, dt)

points = []

#target is a 15 x 15 box
scale = 10/np.max(np.abs([xs, zs]))
xs = scale*xs + scale*np.abs(np.min([xs]))
zs = scale*zs + scale*np.abs(np.min([zs]))

# Plot the results
fig, ax = plt.subplots(figsize=(10,10))
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title(attractor + " Attractor")

ax.plot(xs, zs, lw=0.5, color='purple')
plt.show()

st.pyplot(fig)


#Generate the path
total_dist = 0
for i in range(len(xs) - 1):
    # Calculate the distance in x and y
    dx = xs[i+1] - xs[i]
    dy = zs[i+1] - zs[i]
    distanceBetweenPoints = np.sqrt((dx)**2 + (dy)**2) #in cm
    if i == 1:
        points.append((xs[i], zs[i]))
    if total_dist > 0.5:
        points.append((xs[i], zs[i]))
        total_dist = 0
    else:
        total_dist += distanceBetweenPoints

path = [points]

st.write('''Our robot takes in a data set of the path you want it to follow, hit the following button to create the dataset.''')

# Create a button
button_pressed1 = st.button('Create Robot Path')
if button_pressed1:
    # Create a figure and axis for the scatter plot
    fig1, ax = plt.subplots()

    # Plot the scatter plot
    scatter = ax.scatter(xs, zs, c=zs, cmap='inferno', s=1)

    # Set the axis limits
    ax.set_xlim(np.min(xs), np.max(xs))
    ax.set_ylim(np.min(zs), np.max(zs))

    # Set the axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Z')

    # Set the title
    ax.set_title(attractor + " Attractor")

    # Display the scatter plot
    st.pyplot(fig1)

# Create a Streamlit figure and plot the data
fig, ax = plt.subplots()
ax.set_title(attractor + " Attractor Path")
ax.set_xlabel('x')
ax.set_ylabel('z')

# Set the fixed maximum x and y limits
max_x = np.max(xs)
max_y = np.max(zs)
ax.set_xlim(-max_x, max_x)
ax.set_ylim(-max_y, max_y)

# Create a placeholder for the plot
plot_placeholder = st.empty()

st.write('''Now to witness the movement of the algorithm through a robotic demonstration hit Print!''')

# Create a button
button_pressed = st.button('Print')

if button_pressed:
    getPoints('SVG/Chaos1.svg',path)
    for i in range(len(path)-1):
        ax.cla()  # Clear the previous plot
        ax.set_xlim(-max_x, max_x)  # Set x limits
        ax.set_ylim(-max_y, max_y)  # Set y limits
        ax.plot(path[:i+1][0], path[:i+1][1], color='blue', lw=0.5)
        # Get the current edge position
        current_edge_x = path[i, 0]
        current_edge_y = path[i, 1]

        # Plot a red dot at the current edge position
        ax.plot(current_edge_x, current_edge_y, 'ro')
        plot_placeholder.pyplot(fig)
    plt.close(fig)

st.subheader("References")
st.write('https://www.dynamicmath.xyz/strange-attractors/')
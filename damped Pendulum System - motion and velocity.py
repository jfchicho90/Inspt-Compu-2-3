import matplotlib.pyplot as plt
import numpy as np

#variables and constants

velocity = 0
position = 79
g = -9.81
t = 0
timelapse = 28 
#28 seconds of oscillations
dt = 0.05
b = 0.2
lengthString = 10

fig, ax = plt.subplots(3)

#euler method
def motionAndVelocity_curves(velocity, position, t):
    while t < timelapse:
        acceleration = -(g/lengthString)*np.sin(position) - b*velocity
        velocity = velocity + acceleration*dt
        ax[0].plot(t, position, ".r")
        ax[1].plot(t, velocity, ".b")
        ax[2].plot(position, velocity, ".y")
        position = position + velocity*dt
        t = t + dt
        
ax[0].set_title("Position vs time")
ax[1].set_title("Velocity vs time")
ax[2].set_title("Phase diagram")

motionAndVelocity_curves(velocity, position, t)

plt.show()
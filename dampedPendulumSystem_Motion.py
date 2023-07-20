import matplotlib.pyplot as plt
import numpy as np

#variables and constants
velocity = 0
position = 79
g = -9.81
t = 0
timelapse = 25
dt = 0.05
b = 0.2
lengthString = 10

#function to define the particle's angular position
def motion_curve(velocity, position, t):
    while t < timelapse:
        acceleration = -(g/lengthString)*np.sin(position) - b*velocity
        velocity = velocity + acceleration*dt
        plt.plot(t, position, ".r")
        position = position + velocity*dt
        t = t + dt
        
motion_curve(velocity, position, t)

plt.show()
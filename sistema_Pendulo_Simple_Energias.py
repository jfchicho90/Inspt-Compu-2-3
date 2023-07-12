import matplotlib.pyplot as plt
import numpy as np

theta_posicion = 5
theta_velocidad = 0
L = 5
g = 9.81
t = 0
dt = 0.01
m = 0.01

def pendulo_Simple(theta_posicion, theta_velocidad, g, L, dt, t, m):
    while t < 5:
        a = -(g/L)*(theta_posicion)
        theta_velocidad = theta_velocidad + a*dt
        theta_posicion = theta_posicion + theta_velocidad*dt
        plt.plot(t, 0.5*m*theta_velocidad**2, ".b", t, m*g*(L)*(1 - np.cos(theta_posicion)), ".r")
        t = t + dt
        
pendulo_Simple(theta_posicion, theta_velocidad, g, L, dt, t, m)

plt.show()

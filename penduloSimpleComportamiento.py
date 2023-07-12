import matplotlib.pyplot as plt
import numpy as np

#variables y constantes
v = 0
theta = 5
dT = 0.01
t = 0
L = 5
g = -9.81

#funcion
def sistema_Pendulo_Simple_Comportamiento(theta, v, t):
    while(t < 10):
        thetaA = (g/L)*theta
        v = v + thetaA*dT
        plt.plot(t, theta, ".g")
        theta = theta + v*dT
        t = t + dT
        
#invocacion        
sistema_Pendulo_Simple_Comportamiento(theta, v, t)

#grafica
plt.show()

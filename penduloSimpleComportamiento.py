import matplotlib.pyplot as plt
import numpy as np

#variables y constantes
velocidad_angular = 0
posicion_angular = 45
dT = 0.01
t = 0
L = 5
g = -9.81

#funcion
def sistema_Pendulo_Simple_Comportamiento(t, posicion_angular, velocidad_angular):
    while(t < 10):
        a = (g/L)*posicion_angular 
        velocidad_angular = velocidad_angular + a*dT
        plt.plot(t, posicion_angular, ".g")
        posicion_angular = posicion_angular + velocidad_angular*dT
        t = t + dT
        
#invocacion        
sistema_Pendulo_Simple_Comportamiento(t, posicion_angular, velocidad_angular)

#grafica
plt.show()

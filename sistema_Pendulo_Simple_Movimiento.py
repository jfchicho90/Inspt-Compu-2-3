import matplotlib.pyplot as plt

#variables y constantes
velocidad_angular = 0
posicion_angular = 5
tiempo_Oscilacion = 15
dT = 0.01
t = 0
L = 5
g = -9.81

#funcion
def sistema_Pendulo_Simple_Comportamiento(t, tiempo_Oscilacion, posicion_angular, velocidad_angular):
    while(t < 10):
        a = (g/L)*posicion_angular 
        velocidad_angular = velocidad_angular + a*dT
        plt.plot(t, posicion_angular, ".g")
        posicion_angular = posicion_angular + velocidad_angular*dT
        t = t + dT
        
#invocacion        
sistema_Pendulo_Simple_Comportamiento(t, tiempo_Oscilacion, posicion_angular, velocidad_angular)

#grafica
plt.show()

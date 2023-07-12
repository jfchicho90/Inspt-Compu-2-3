import matplotlib.pyplot as plt

def pendulo_Simple(tiempo_Oscilacion, posicion_angular, velocidad_angular, t, m, L):
    while t < tiempo_Oscilacion:
        a = -(g/L)*(posicion_angular)
        velocidad_angular = velocidad_angular + a*dt
        posicion_angular = posicion_angular + velocidad_angular*dt
        plt.plot(t, 0.5*m*velocidad_angular**2, ".b")
        t = t + dt

#variables y constantes
posicion_angular = 5
velocidad_angular = 0
t = 0
tiempo_Oscilacion = 15
L = 5
g = 9.81
dt = 0.01
m = 0.3

#invocacion 
pendulo_Simple(tiempo_Oscilacion, posicion_angular, velocidad_angular, t, m, L)

#grafica
plt.show()



import matplotlib.pyplot as plt

#declaraciones
def caidaLibre(t, x, v, a, dt, m, tiempo_Vuelo):
    while t < tiempo_Vuelo:
        v = v + a*dt
        x = x + (v*dt + 0.5*a*dt**2)
        plt.plot(t, x, ".r")
        plt.plot(t, v, ".b")
        plt.title("Posiciones y velocidades")
        t = t + dt

#variables
#velocidad inicial 0
v = 0
x = 100
t = 0
dt = 0.01
a = -9.81
m = 1
tiempo_Vuelo = 15

#euler
caidaLibre(t, x, v, a, dt, m, tiempo_Vuelo)

#grafica
plt.legend(["Posicion", "Velocidad"], loc ="lower left")
plt.show()
import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt

viscosidad_vertical = 0.019

densidad = 1025

coriolis = 0.0007

efecto_viento = 0.4

altura_inicial = 0

altura_profundidad = -50

pasos = 0.002

altura = np.arange(altura_profundidad, altura_inicial, pasos)
def ekman_giro(altura):
  ekman = np.pi*((2*viscosidad_vertical)/coriolis)**0.5
  Vcero = ((2**0.5)*np.pi*efecto_viento)/(ekman*densidad*coriolis)
  
  uE = -Vcero*np.cos(np.pi/4 + altura*np.pi/ekman)*np.exp(np.pi/ekman*altura)
  vE = Vcero*np.sin(np.pi/4 + np.pi/ekman*altura)*np.exp(np.pi/ekman*altura)
 
  fig, ax = plt.subplots(1, sharex=True, sharey=True)
  colores = altura
  normal = mlp.colors.Normalize(altura_profundidad, altura_inicial)

  plt.scatter(vE, uE, c = colores, cmap="plasma", s = 5, norm = normal)
  plt.colorbar()

  ax.set_xlabel('Velocidad zonal [m/s]')
  ax.set_ylabel('Velocidad meridional [m/s]')

ekman_giro(altura)

plt.show()

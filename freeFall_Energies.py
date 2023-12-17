import matplotlib.pyplot as plt

#The initial velocity is zero and the mass falls from a height of 500 meters.
#The graphs show both kinetic and potential energy until mass hits the ground.

v = 0
y = 500
t = 0
dt = 0.1
a = -9.81
m = 0.3

def freeFall_EulerMethod(t, y, v, a):
    fig, ax = plt.subplots(2)
    while y > 0:
        v = v + a*dt
        y = y + (v*dt + 0.5*a*dt**2)
        ax[0].plot(t, 0.5*m*v**2, ".r")
        ax[1].plot(t, -m*a*y, ".b")
        t = t + dt
    ax[0].set_title('Kinetic energy')
    ax[1].set_title("Potential energy")
   
     
#euler
freeFall_EulerMethod(t, y, v, a)

plt.show()

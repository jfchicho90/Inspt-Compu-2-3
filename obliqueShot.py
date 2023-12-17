import matplotlib.pyplot as plt

y = 0
v = 10
t = 0
g = -9.81
m = 2
dt = 0.001
vx = 7
vy = 10
x = 0

 def obliqueShot(t, x, y, vx, vy):
  while y >= 0:
    vx = vx + g*dt
    vy = vy + g*dt
    y = y + (vy*dt + 0.5*g*(t**2))
    x = x + vx*dt
    plt.plot(x, y, ".r")
    t = t + dt
  plt.title("oblique shot")

obliqueShot(t, x, y, vx, vy)
plt.show()

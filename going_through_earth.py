import matplotlib.pyplot as plt

#Data
earth_radius = 6371000
m = 70
earth_mass = 5.972*10**24
position = earth_radius
t = 0
G = -6.674*10**-11
v = 0
dt = 10
estimated_time = 2800

def defining_Gravity(position): #Acceleration of the particle as it goes through earth
    acceleration = (earth_mass*position*G)/(earth_radius**3)
    return  acceleration

def potential_energy_curve(position, gravity):
    return -m*defining_Gravity(position)*position

def kinetic_energy_curve(velocity):
    return 0.5*m*velocity**2

def time_of_arrival(t, position, v):
    fig, ax = plt.subplots(3)
    while earth_radius + position >= 0:
        gravity = defining_Gravity(position) #Invoking the acceleration of the particle depending on the position
     
        ax[0].plot(t, abs(position), ".b") #Plotting the position as the particles goes through earth
        ax[1].plot(t, kinetic_energy_curve(v), ".r")
        ax[2].plot(t, potential_energy_curve(position, gravity), ".g")

        v = v + gravity*dt 
        
        position = position + v*dt
        
        arrival_time = t/3600
        
        t = t + dt
    return arrival_time
        
time = time_of_arrival(t, position, v)
print("Time for travelling throuth Earth:", time, " hours")
plt.show()
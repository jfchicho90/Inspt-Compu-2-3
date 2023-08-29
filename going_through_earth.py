import matplotlib.pyplot as plt

#Data
earth_radius = 6371000
m = 70 #mass of the particle
earth_mass = 5.972*10**24
position = earth_radius
t = 0
G = -6.674*10**-11 #Gravitational constant
v = 0 #Initial velocity
dt = 10

def defining_Gravity(position): 
    acceleration = (earth_mass*position*G)/(earth_radius**3) 
    #Acceleration of the particle as it passes through earth
    return  acceleration

def potential_energy_curve(position, gravity):
    return -m*defining_Gravity(position)*position

def kinetic_energy_curve(velocity):
    return 0.5*m*velocity**2

def time_of_arrival(t, position, v):
    fig, ax = plt.subplots(3) #Three different graphs
    while earth_radius + position >= 0:
        gravity = defining_Gravity(position) 
        #Invoking the acceleration of the particle depending on the position
     
        ax[0].plot(t, abs(position), ".b") 
        ax[0].set_title("Position in time")
        #Plotting the particle´s position as it goes through earth
        ax[1].plot(t, kinetic_energy_curve(v), ".r")
        ax[1].set_title("Kinetic energy")
        ax[2].plot(t, potential_energy_curve(position, gravity), ".g")
        ax[2].set_title("Potential energy")
        
        v = v + gravity*dt 
        
        position = position + v*dt
        
        arrival_time = t/3600
        
        t = t + dt
    return arrival_time
        
time = time_of_arrival(t, position, v)
print("Time for reaching the opposite end of earth:", time, " hours")
plt.show()

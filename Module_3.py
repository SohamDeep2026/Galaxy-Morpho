import math
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np

# Simulation parameters
TIME_STEP = 0.01    # Size of each Euler integration step
N = 15              # Number of particles along one side of the grid (total N*N)
G = 1               # Gravitational Const

index = range(N * N)

x = [0,0]   
y = [0,1]   
mass = [10,1]  

v_x = [1,0]  
v_y = [0,0]  

# Clear lists to reset
x.clear()
y.clear()
v_x.clear()
v_y.clear()
mass.clear()

# Initialize particles on a square grid centered at origin
for i in index:
    x.append((i % N) - (N - 1)/2)                
    y.append(math.floor((i / N) % N) - (N - 1)/2) 
    mass.append(1)

# Initialize particle velocities
for i in range(len(x)):
  
#code for zero motion
    # v_y.append(0)
    # v_x.append(0)

#code for circular motion  
    v_y.append((3 * x[i]))
    v_x.append(-3 * y[i])

#code for shearing motion
    # v_y.append(x[i])
    # v_x.append(0)

a_x = []
a_y = []

potential_energy = 2


# Compute net acceleration from all other particles
def calculate_acc(x, y):
    a_x.clear()
    a_y.clear()


    for i in range(len(x)):
        sum_x = 0
        sum_y = 0

        
        for j in range(len(x)):

            if i == j:
                continue 

          
            distance = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)

            if distance > 0.001:
        
                sum_x += G * mass[j] * (x[j] - x[i]) / distance**2
                sum_y += G * mass[j] * (y[j] - y[i]) / distance**2

            else:
                # Handle very close particles by merging velocities (assume inelastic collision)
                v_x[i] = (v_x[i] + v_x[j]) / 2
                v_y[i] = (v_y[i] + v_y[j]) / 2
                v_x[j] = (v_x[i] + v_x[j]) / 2
                v_y[j] = (v_y[i] + v_y[j]) / 2

        a_x.append(sum_x)
        a_y.append(sum_y)


       
# def runge_kutta_4(p, v, a, h):
#     k1 = h * v
#     l1 = h * calculate_acc(p)
#     k2 = h * (v + l1/2)



# Compute initial accelerations
calculate_acc(x, y)
# Setup matplotlib figure
fig, ax = plt.subplots()
point, = ax.plot(x, y, 'o',)

# Update function called at each animation frame
def update(frame):


    calculate_acc(x, y)
    
    ang_momentum = 0
    kinetic_energy = 0
    
    # Update particle velocities and positions (Euler integration)
    for i in range(len(x)):
        v_x[i] += a_x[i] * TIME_STEP
        x[i] += v_x[i] * TIME_STEP

        v_y[i] += a_y[i] * TIME_STEP
        y[i] += v_y[i] * TIME_STEP

        # Track angular momentum and kinetic energy for diagnostics
        ang_momentum += v_y[i] * x[i] + v_x[i] * y[i]
        kinetic_energy += 0.5 * mass[i] * (v_y[i]**2 + v_x[i]**2)

    print("Angular Momentum: ", ang_momentum, "Kinetic Energy: ", kinetic_energy)

    # Update particle positions on plot
    point.set_data(x, y)

    return point,

# Animate simulation
animation = anim.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Set viewing window

Scale = 3
ax.set_xlim(-Scale * N, Scale * N)
ax.set_ylim(-Scale * N, Scale * N)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

from simulations.body_2 import main

all_positions = main(delta_t=0.001, steps=5000)

# Number of moments and objects
num_positions, num_objects, num_dim = all_positions.shape

# Extract x (time) and y (coordinate) values

# Plot
plt.figure(figsize=(8, 5))

# Line plot
for obj_id in range(num_objects):
    xpos = all_positions[:, obj_id, 0]
    ypos = all_positions[:, obj_id, 1]
    plt.plot(xpos, ypos, marker='o', linestyle='-', label=f'Object {obj_id+1}')

# Labels and legend
plt.xlabel('X-Coordinate')
plt.ylabel('Y-Coordinate')
plt.title('Object Motion In Space')
plt.legend()
plt.grid(True)

# Show plot
plt.show()

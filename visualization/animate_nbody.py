import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from simulations.body_3 import main

# Assuming all_positions is already defined from `main()`
all_positions = main(delta_t=0.01, steps=10000)

# Number of moments and objects
num_positions, num_objects, num_dim = all_positions.shape

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Set axis limits based on data
x_min, x_max = np.min(all_positions[:, :, 0]), np.max(all_positions[:, :, 0])
y_min, y_max = np.min(all_positions[:, :, 1]), np.max(all_positions[:, :, 1])
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Initialize plot elements
lines = [ax.plot([], [], marker='o', linestyle='-')[0] for _ in range(num_objects)]
scatters = [ax.scatter([], [], s=50, label=f'Object {i+1}') for i in range(num_objects)]

# Update function for animation
def update(frame):
    for obj_id in range(num_objects):
        xpos = all_positions[:frame+1, obj_id, 0]  # Include up to current frame
        ypos = all_positions[:frame+1, obj_id, 1]

        # Update line (trajectory)
        lines[obj_id].set_data(xpos, ypos)

        # Ensure scatter gets a valid shape (M, 2)
        if len(xpos) > 0:
            scatters[obj_id].set_offsets(np.column_stack((xpos[-1:], ypos[-1:])))
        else:
            scatters[obj_id].set_offsets(np.zeros((1, 2)))  # Safe default

    return lines + scatters

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_positions, interval=10, blit=True)

# Labels and legend
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Object Motion Over Time')
plt.legend()
plt.grid(True)

# Show animation
plt.show()

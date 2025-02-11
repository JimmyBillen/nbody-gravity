import json
import numpy as np

def energy_calculator(velocities_dir: list[np.ndarray], mass):
    """Calculates the total energy, using velocity in every direction. (Multi-dim)"""
    energy_sqrd = 0 
    for velocities in zip(*velocities_dir):
        energy_sqrd = sum([0.5 * mass * velocity**2 for velocity in velocities])
    return np.sqrt(energy_sqrd)

def save_simulation(positions, filename="simulation.json"):
    with open(filename, "w") as f:
        json.dump(positions.tolist(), f)

def load_simulation(filename):
    with open(filename, "r") as f:
        return np.array(json.load(f))

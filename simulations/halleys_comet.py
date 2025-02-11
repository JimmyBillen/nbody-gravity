import numpy as np

from src.nbody import NBodySimulation

def main(delta_t = None, steps = None):
    """Simulate Halleys Comet"""
    if delta_t is None:
        # single orbit takes many years, so dt = 1 day
        delta_t = 3600 * 24
    if steps is None:
        steps = 100

    # Start at aphelion
    mass_sun = 2e30   # kg
    mass_halley = 2.2e14  # kg
    body_masses = [mass_sun, mass_halley]

    
    start_coordinate_sun = [0, 0]  # m(eter)
    start_coordinate_halley = [5.28e12, 0]  # m 
    init_body_positions = [start_coordinate_sun, start_coordinate_halley]

    start_speed_sun = [0, 0] # m/s
    start_speed_halley = [0, 9.13e2] # m/s
    init_body_velocities = [start_speed_sun, start_speed_halley]

    sim = NBodySimulation(initial_positions=init_body_positions, initial_velocities=init_body_velocities, body_masses=body_masses, delta_t=delta_t)
    positions = sim.run(steps=steps)

    print("Final positions:\n", positions[-1])  # Last step positions
    return positions

if __name__ == "__main__":
    main(steps=1)

import numpy as np

from src.nbody import NBodySimulation

def main(delta_t = None, steps = None):
    if delta_t is None:
        delta_t = 1
    if steps is None:
        steps = 100

    # Start at aphelion
    mass1 = 1 # kg
    mass2 = 1.5 # kg
    mass3 = 2 # kg
    body_masses = [mass1, mass2, mass3]

    grav_constant = 1
    # G = 6.67428e-11
    # body_masses = [ ( 1 / G ) * mass for mass in body_masses]
    
    start_coordinate1 = [3, 0]  # m(eter)
    start_coordinate2 = [-3, 0]  # m 
    start_coordinate3 = [0, 3]  # m 
    init_body_positions = [start_coordinate1, start_coordinate2, start_coordinate3]

    start_speed1 = [0, 0]
    start_speed2 = [0, 0] # m/s
    start_speed3 = [0, 0] # m/s
    init_body_velocities = [start_speed1, start_speed2, start_speed3]

    radius1 = 0.3
    radius2 = 0.3
    radius3 = 0.3
    radii = [radius1, radius2, radius3]

    sim = NBodySimulation(initial_positions=init_body_positions, initial_velocities=init_body_velocities, body_masses=body_masses, grav_constant = grav_constant, delta_t=delta_t, body_radius=radii)
    positions = sim.run(steps=steps)

    print("Final positions:\n", positions[-1])  # Last step positions
    return positions

if __name__ == "__main__":
    main(steps=1)
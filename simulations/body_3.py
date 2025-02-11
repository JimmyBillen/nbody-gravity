import numpy as np

from src.nbody import NBodySimulation

def main(delta_t = None, steps = None):
    """Simulate Halleys Comet"""
    if delta_t is None:
        # single orbit takes many years, so dt = 1 day
        delta_t = 1
    if steps is None:
        steps = 100

    # Start at aphelion
    mass1 = 1 # kg
    mass2 = 1.5 # kg
    mass3 = 2 # kg
    body_masses = [mass1, mass2, mass3]
    G = 6.67428e-11
    body_masses = [ ( 1 / G ) * mass for mass in body_masses]
    
    start_coordinate1 = [3, 0]  # m(eter)
    start_coordinate2 = [-3, 0]  # m 
    start_coordinate3 = [0, 3]  # m 
    init_body_positions = [start_coordinate1, start_coordinate2, start_coordinate3]

    start_speed1 = [0, 0]
    start_speed2 = [0, 0] # m/s
    start_speed3 = [0, 0] # m/s
    init_body_velocities = [start_speed1, start_speed2, start_speed3]

    sim = NBodySimulation(initial_positions=init_body_positions, initial_velocities=init_body_velocities, body_masses=body_masses, delta_t=delta_t)
    positions = sim.run(steps=steps)

    print("Final positions:\n", positions[-1])  # Last step positions
    return positions

if __name__ == "__main__":
    main(steps=1)

    # with three of them nice! At the end divergence
    # mass1 = 1 # kg
    # mass2 = 1 # kg
    # mass3 = 1 # kg
    # body_masses = [mass1, mass2, mass3]
    # G = 6.67428e-11
    # body_masses = [ ( 1 / G ) * mass for mass in body_masses]
    
    # start_coordinate1 = [8, 1]  # m(eter)
    # start_coordinate2 = [4, 4]  # m 
    # start_coordinate3 = [9, 6]  # m 
    # init_body_positions = [start_coordinate1, start_coordinate2, start_coordinate3]

    # start_speed1 = [-0.1, -0.1]
    # start_speed2 = [0, 0.1] # m/s
    # start_speed3 = [-0.1, 0.1] # m/s
    # init_body_velocities = [start_speed1, start_speed2, start_speed3]

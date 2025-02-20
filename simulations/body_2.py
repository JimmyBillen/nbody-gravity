import numpy as np

from src.nbody import NBodySimulation

def main(delta_t = None, steps = None):
    if delta_t is None:
        # single orbit takes many years, so dt = 1 day
        delta_t = 1
    if steps is None:
        steps = 100

    # Start at aphelion
    mass1 = 10 # kg
    mass2 = 1 # kg
    body_masses = [mass1, mass2]
    # G = 6.67428e-11
    # body_masses = [ ( 1 / G ) * mass for mass in body_masses]
    grav_constant = 0
    
    start_coordinate1 = [0, 0]  # m(eter)
    start_coordinate2 = [np.sqrt(18), 0]  # m 
    init_body_positions = [start_coordinate1, start_coordinate2]

    start_speed1 = [np.sqrt(2), 0]
    start_speed2 = [-np.sqrt(18), 0] # m/s
    init_body_velocities = [start_speed1, start_speed2]

    radius1 = 1
    radius2 = 1
    radii = [radius1, radius2]

    sim = NBodySimulation(initial_positions=init_body_positions, initial_velocities=init_body_velocities, body_masses=body_masses, delta_t=delta_t, body_radius=radii, grav_constant=grav_constant)
    positions = sim.run(steps=steps)

    print("Final positions:\n", positions[-1])  # Last step positions
    return positions

if __name__ == "__main__":
    main(steps=1)
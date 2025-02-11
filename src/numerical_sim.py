import numpy as np

from src.physics import gravitational_acceleration


def update_coordinates(positions_multidim: np.ndarray[np.ndarray], velocity_multidim: np.ndarray[np.ndarray], acceleration_multidim: np.ndarray[np.ndarray], delta_t: float, body_masses: np.ndarray, grav_constant: float):
    """Using velocity-verlet algorithm to simulate objects subjected to a force.
    
    args
    ----
    positions_multidim: 
        A list of np.arrays containing the position, each element corresponding to a direction. Shape [[x1, y1,..], [x2, y2,..],...]
    velocity_multidim:
        A list of np.arrays containing the velocity, each element corresponding to a direction. Shape [[vx1, vy1,..], [vx2, vy2,..],...]
    acceleration_multidim:
        A list of np.arrays containing the acceleration, each element corresponding to a direction. Shape [[ax1, ay1,..], [ax2, ay2,..],...]
    delta_t:
        Time step for numerical integration.
    mass:
        An array, containing the mass of each object. 
    """
    new_position = positions_multidim + velocity_multidim * delta_t + 0.5 * acceleration_multidim * delta_t**2
    new_velocity_half = velocity_multidim + 0.5 * acceleration_multidim * delta_t
    new_acceleration = gravitational_acceleration(body_positions=new_position, body_masses=body_masses, grav_constant=grav_constant)
    new_velocity = new_velocity_half + 0.5 * new_acceleration * delta_t

    return new_position, new_velocity, new_acceleration


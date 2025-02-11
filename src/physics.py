import numpy as np

def gravitational_acceleration(body_positions: np.ndarray, body_masses: np.ndarray, grav_constant: float=None) -> np.ndarray:
    """Calculates gravitational force between all other masses in two dimensions
    
    a = G * Mass (mass of bodies that affects object) / Radius (between body that affects it)

    args
    -----
    body_positions: 
        array of positions of the bodies.

    G = 6.67428e-11 # m**3 / (kg * s**2) 
    """


    # Initialize an array to store the total gravitational force for each body.
    total_gravitational_acceleration_each_body = np.zeros_like(body_positions)

    # Calculate the attraction exerted on the main body by each other body
    for index, main_body_position in enumerate(body_positions):
        other_positions = body_positions[np.arange(len(body_positions)) != index]
        other_mass = body_masses[np.arange(len(body_masses)) != index]

        # Calculate the squared distance from the main body to each other body
        distance_vectors = other_positions - main_body_position
        squared_distances = np.sum(np.square(distance_vectors), axis=1)  # Sum across dimensions (x, y, ...)

        # Compute the gravitational force magnitude using Newton's Law: F = G * m / r²
        acceleration_magnitudes = grav_constant * np.divide(other_mass, squared_distances)

        # Normalize direction vectors (unit vectors) to find force components
        unit_vectors = np.divide(distance_vectors, np.sqrt(squared_distances)[:, np.newaxis])

        # Compute gravitational force in each direction
        acceleration_components = unit_vectors * acceleration_magnitudes[:, np.newaxis]

        # Sum the forces from all bodies
        net_gravitational_force = np.sum(acceleration_components, axis=0)

        # Store the result in the first row of total_gravitational_force
        total_gravitational_acceleration_each_body[index] = net_gravitational_force

    return total_gravitational_acceleration_each_body

def two_dim_collision(body_position1, body_position2, body_velocity1, body_velocity2, body_mass1, body_mass2):
    """Calculates the velocities in each direction (x, y) after collision.

    Based on:
    https://en.wikipedia.org/wiki/Elastic_collision#Two-dimensional_collision_with_two_moving_objects
    """
    # writing in shorter variable form
    x1, y1 = body_position1
    x2, y2 = body_position2

    # velocities
    v1x, v1y = body_velocity1
    v2x, v2y = body_velocity2

    m1, m2 = body_mass1, body_mass2

    # calculating movement angle
    theta1 = np.arctan(v1y/v1x)
    theta2 = np.arctan(v2y/v2x)

    # contact angle
    phi = np.arctan( )




if __name__ == "__main__":
    start_coordinate_sun = [0, 0]  # m(eter)
    start_coordinate_halley = [5.28e12, 0]  # m 
    init_body_positions = np.array([start_coordinate_sun, start_coordinate_halley])

    mass_sun = 2e30   # kg
    mass_halley = 2.2e14  # kg
    body_masses = np.array([mass_sun, mass_halley])


    gravitational_acceleration(init_body_positions, body_masses)
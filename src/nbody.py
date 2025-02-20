from src.physics import gravitational_acceleration, two_dim_collision
from src.numerical_sim import update_coordinates, displace_bodies
import numpy as np

# extensibility: for performance purposes there has not been added a class body. Vectorization would be more complex to implement.
# Recommended to add when considering merges of bodies.

class NBodySimulation:
    """Simulates multiple particles under mutual gravitational attraction in a vectorized way."""
    
    def __init__(self, initial_positions, initial_velocities, body_masses, delta_t, grav_constant = 6.67428e-11, body_radius = 6.38e6):
        """
        Args:
        -----
        body_masses : np.ndarray
            1D array of shape (N,) containing masses of N particles.
        initial_positions : np.ndarray
            2D array of shape (N, D) containing positions in D-dimensional space.
        initial_velocities : np.ndarray
            2D array of shape (N, D) containing velocities.
        delta_t : float
            Time step for numerical integration.
        """
        self.body_masses = np.array(body_masses, dtype=float)  # Shape: (N,)
        self.positions = np.array(initial_positions, dtype=float)  # Shape: (N, D)
        self.velocities = np.array(initial_velocities, dtype=float)  # Shape: (N, D)
        self.delta_t = delta_t
        self._G = grav_constant
        self.radius = np.array(body_radius, dtype=float)  # Shape: (N,)

        # Compute initial accelerations
        self.accelerations = gravitational_acceleration(self.positions, self.body_masses, self._G)

    def update_positions(self):
        new_positions, new_velocities, new_accelerations = update_coordinates(
            self.positions,
            self.velocities,
            self.accelerations,
            self.delta_t,
            self.body_masses,
            self._G
        )

        self.positions = new_positions
        self.velocities = new_velocities
        self.accelerations = new_accelerations

    def check_for_collision(self):
        for i in range(len(self.body_masses)):
            for j in range(i+1, len(self.body_masses)):
                dist = np.linalg.norm(self.positions[i] - self.positions[j])
                if dist < self.radius[i] + self.radius[j]:
                    momentum_before = self.body_masses[i] * self.velocities[i] + self.body_masses[j] * self.velocities[j]
                    self.velocities[i], self.velocities[j] = two_dim_collision(
                        body_position1 = self.positions[i],
                        body_position2 = self.positions[j],
                        body_velocity1 = self.velocities[i],
                        body_velocity2 = self.velocities[j],
                        body_mass1 = self.body_masses[i],
                        body_mass2 = self.body_masses[j]
                    ), two_dim_collision( # switch indices in calculation for velocity of other
                        body_position1 = self.positions[j],
                        body_position2 = self.positions[i],
                        body_velocity1 = self.velocities[j],
                        body_velocity2 = self.velocities[i],
                        body_mass1 = self.body_masses[j],
                        body_mass2 = self.body_masses[i]
                    )
                    self.positions[i], self.positions[j] = displace_bodies(
                        self.positions[i],
                        self.positions[j],
                        self.radius[i],
                        self.radius[j],
                        self.body_masses[i],
                        self.body_masses[j]
                    )
                    # after collision should not be in each others radii anymore
                    self.positions[i], self.positions[j] = displace_bodies(
                        self.positions[i],
                        self.positions[j],
                        self.radius[i],
                        self.radius[j],
                        self.body_masses[i],
                        self.body_masses[j]
                    )
                    momentum_after = self.body_masses[i] * self.velocities[i] + self.body_masses[j] * self.velocities[j]
                    

    def run(self, steps):
        """Runs the simulation for a given number of steps and returns positions over time."""
        positions_over_time = []

        for _ in range(steps):
            self.update_positions()
            positions_over_time.append(self.positions.copy())
            self.check_for_collision()

        return np.array(positions_over_time)  # Shape: (steps, N, D)

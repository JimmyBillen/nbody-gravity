import matplotlib.pyplot as plt
from simulations.halleys_comet import main

start_coordinate_sun = [0, 0]  # m(eter)
start_coordinate_halley = [5.28e12, 0]  # m 

plt.scatter(start_coordinate_sun[0], start_coordinate_sun[1], color='red', alpha=0.5)
plt.scatter(start_coordinate_halley[0], start_coordinate_halley[1], color='black', alpha=0.5)

# all_positions = main(steps=365*100)
all_positions = main(steps=365*60)
print(all_positions)
print(all_positions.shape)

sun_x = all_positions[:,0,0]
sun_y = all_positions[:,0,1]
halley_x = all_positions[:,1,0]
halley_y = all_positions[:,1,1]


plt.plot(sun_x, sun_y, color='red', label="sun")
plt.plot(halley_x, halley_y, color='grey', label="comet")

plt.scatter(sun_x[-1], sun_y[-1], color='red')
plt.scatter(halley_x[-1], halley_y[-1], color='black')

plt.legend()
plt.title("movement of comet around the sun for 100 years")
plt.show()

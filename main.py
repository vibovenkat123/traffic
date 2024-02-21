from IDMModel import IDM, Simulation
import matplotlib.pyplot as plt
import pandas as pd
import pyarrow
from Traffic import Traffic

car1 = IDM(x_0=20, v_i=20, v0=25, a=1.7, b=2, s0=2, car_front=None, headway=1, l=4.5)
car2 = IDM(x_0=0, v_i=20, v0=26, a=1.7, b=2, s0=2, car_front=car1, headway=1, l = 4.5)
traffic = [Traffic(x=860, green=60, yellow=6, red=40)]
simulation = Simulation(cars=[car1, car2], t_final=300, traffic_lights=traffic)

simulation.simulate()

print(car2.v, car2.x, car1.v, car1.x)

plt.plot(simulation.t_arr, car2.x_arr)
plt.show()

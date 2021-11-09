import matplotlib.pyplot as plt
import numpy as np

nx_list = []
ny_list = []
# plot 1
x = input("Please Enter the X value for Pulse: ")
y = input("Please Enter the Y value for the Pulse: ")
nx_list.append(x)
ny_list.append(y)

nx_list = np.array(nx_list)
ny_list = np.array(ny_list)

plt.xlim(1, 11)
plt.ylim(10, 70)
plt.plot(nx_list, ny_list, '*')

plt.grid()
plt.show()

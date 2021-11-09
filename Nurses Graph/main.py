import matplotlib.pyplot as plt
from datetime import datetime, date, time

# plot 1:
# These codes help with inputing values
x = input('Enter a number for the Respiration Graph')
nx_list = []
nx_list.append(x)
y = input('Enter a number for the Respiration Graph')
ny_list = []
ny_list.append(y)
# these codes are responsible for ploting the graph
plt.subplot(1, 3, 1)
plt.plot(nx_list, ny_list, '*')

plt.grid()
# this is to display the name of the graph
plt.title('Respiration')
# plot 2:
# These codes help with inputing values
x = input('Enter a number for the Pulse Graph')
nx_1_list = []
nx_1_list.append(x)
y = input('Enter a number for the Pulse Graph')
ny_1_list = []
ny_1_list.append(y)
# these codes are responsible for ploting the graph
plt.plot(nx_1_list, ny_1_list, '*')
plt.subplot(1, 3, 2)

plt.grid()

# this is to display the name of the graph
plt.title('Pulse Graph')

# plot 3:

# These codes help with inputing values
x = input('Enter a number for the Temperature Graph')
nx_2_list = []
nx_list.append(x)
y = input('Enter a number for the Temperature Graph')
ny_2_list = []
ny_list.append(y)
# These codes help with inputing values
plt.plot(ny_2_list, ny_2_list, '*')
plt.subplot(1, 3, 3)

plt.grid()
# this is to display the name of the graph
plt.title('Temperature')
# this is to show the graph

plt.show()

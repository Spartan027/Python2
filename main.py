import matplotlib.pyplot as plt
from datetime import datetime,date,time


#plot 1:
#These codes help with inputing values
x = input('Enter a number for the Respiration Graph')
nx_list = []
nx_list.append(x)
y = input('Enter a number for the Respiration Graph')
ny_list = []
ny_list.append(y)
#these codes are responsible for ploting the graph
plt.plot(x, y, '*')
plt.subplot(1, 3, 1)
plt.plot(x, y, '*')
plt.xlim(1, 11)
plt.ylim(0, 60)
plt.grid()
#this is to display the name of the graph
plt.title('Respiration')
 #plot 2:
#These codes help with inputing values
x = input('Enter a number for the Pulse Graph')
nx_list = []
nx_list.append(x)
y = input('Enter a number for the Pulse Graph')
ny_list = []
ny_list.append(y)
#these codes are responsible for ploting the graph
plt.plot(x, y, '*')
plt.subplot(1, 3, 2)
plt.plot(x, y, '*')
plt.xlim(1, 11)
plt.ylim(60, 180)
plt.grid()
#this is to display the name of the graph
plt.title('Pulse Graph')
 #plot 3:
#These codes help with inputing values
x = input('Enter a number for the Temperature Graph')
nx_list = []
nx_list.append(x)
y = input('Enter a number for the Temperature Graph')
ny_list = []
ny_list.append(y)
#These codes help with inputing values
plt.plot(x, y, '*')
plt.subplot(1, 3, 3)
plt.plot(x, y, '*', )
plt.xlim(1, 11)
plt.ylim(35, 41)
plt.grid()
#this is to display the name of the graph
plt.title('Temperature')
#this is to show the graph
plt.show()

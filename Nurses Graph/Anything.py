import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


class Hospitalization:
    Pulse = []
    Temperature = []
    Respiration = []
    Oxygen = []
    DateTime = []

    def getTime(self):
        now = datetime.now()
        now = now.strftime('%H:%M:%S')
        self.DateTime.append(now)

    def pulse_function(self):
        pr = input("Please Enter the Y value for the Pulse: ")
        self.Pulse.append(pr)
        plt.subplot(1, 4, 1)
        plt.title("Pulse")
        plt.plot(self.DateTime,self.Pulse,marker="*")

    def temperature_function(self):
        temp = input("Please Enter the value for Temperature")
        self.Temperature.append(temp)
        plt.subplot(1, 4, 2)
        plt.title("Temperature")
        plt.plot(self.DateTime,self.Temperature,marker="*")



    def respiration_function(self):
        resp = input("Please Enter the value for Respiration")
        self.Respiration.append(resp)
        plt.subplot(1, 4, 3)
        plt.title("Respiration")
        plt.plot(self.DateTime,self.Respiration,marker="*")

    def oxygen_function(self):
        oxy = input("Please Enter the value for Oxygen")
        self.Oxygen.append(oxy)
        plt.subplot(1, 4, 4)
        plt.title("Oxygen")
        plt.plot(self.DateTime,self.Oxygen,marker="*")

g1 = Hospitalization()
true = 1
while true:
    g1.getTime()
    g1.pulse_function()
    g1.temperature_function()
    g1.respiration_function()
    g1.oxygen_function()
    plt.show()

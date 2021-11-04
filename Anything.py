import matplotlib.pyplot as plt
from datetime import datetime, date, time
import numpy


class PlotGraph:

    input_values = []
    date_values = []

    def plot_a_graph(self):
        ans = input('Enter the number of inputs you want to accept: ')
        # ns = int(ans)

        for a in range(ans):
            value = input('Enter value: ' + str(a+1))
            value = int(value)
            now = datetime.now()
            self.date_values.append(now)
            self.input_values.append(value)
        plt.plot(self.date_values, self.input_values)
        plt.show()
        co = self.date_values.copy()


p1 = PlotGraph()
p1.plot_a_graph()



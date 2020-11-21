import matplotlib.pyplot as plt
import numpy as np

class Plot():
    def __init__(self):
        self.plt = plt
        self.fig, self.ax = self.plt.subplots()


    def scat(self, scatters):
        x = [x[0] for x in scatters]
        y = [y[1] for y in scatters]
        self.ax.scatter(x, y)

    def show(self):
        self.plt.show()


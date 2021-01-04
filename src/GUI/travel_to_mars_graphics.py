import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import matplotlib.animation as animation


class TravelToMarsGraphics(object):

    def __init__(self):
        # self.hohmann_transfer_orbit = hohmann
        # self.mission = hohmann.mission
        # self.spacecraft = hohmann.spacecraft
        self.init_scales()

    def animate(self, i):
        hehe = plt.plot(3,4)
        return hehe

    def init_scales(self):
        fig, ax = plt.subplots(figsize=(10, 8))
        plt.plot(0, 0, "D-")
        plt.annotate("sun", (0, 0.1))

        plt.plot(0, 0.5, "D-")
        plt.annotate("earth", (0, 0.6))

        plt.plot(0, 1, "D-")
        plt.annotate("mars", (0, 1.1))
        # Set axis ranges; by default this will put major ticks every 25.
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)

        # Change major ticks to show every 20.
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(1))

        # Change minor ticks to show every 5. (20/4 = 5)
        ax.xaxis.set_minor_locator(AutoMinorLocator(10))
        ax.yaxis.set_minor_locator(AutoMinorLocator(10))

        # Turn grid on for both major and minor ticks and style minor slightly
        # differently.
        ax.grid(which='major', color='#CCCCCC', linestyle='--')
        ax.grid(which='minor', color='#CCCCCC', linestyle=':')
        anim = animation.FuncAnimation(fig, self.animate, frames=365, interval=55)
        plt.show()

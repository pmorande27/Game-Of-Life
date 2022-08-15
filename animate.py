from Game import Game
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors
from matplotlib import patches
class Animation(object):
    def __init__(self, pattern):
        """
        Consturctor of the Animation class
        """
        self.game = Game(pattern)

    def updatefig(self,i):
        """
        Method used to update the system for animation
        """
        print(i)
        self.game.evolve()
        self.im.set_array(self.game.lattice)
        return [self.im]

    def init(self):
        """
        Method used to init the animation
        """
        self.im = plt.imshow(self.game.lattice,cmap='Greys')
        return [self.im]

    def animation(self):
        """
        Method used to create an animation of the model
        """
        fig = plt.figure()
        ani = animation.FuncAnimation(fig, self.updatefig,init_func=self.init,interval = 100, blit = True)
        plt.show()        
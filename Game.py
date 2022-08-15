import matplotlib.pyplot as plt
from scipy.ndimage import convolve,generate_binary_structure
import numpy as np
class Game():
    def __init__(self, pattern):

        self.dimension_vertical = len(pattern)
        self.dimension_horizontal = len(pattern[0])
        if self.dimension_horizontal*self.dimension_vertical != len(pattern.flatten()):
            raise ValueError() 
        self.lattice = pattern

    def evolve(self):
        kernel = generate_binary_structure(2,2)
        kernel[1][1] = False
        neighbour_matrix = convolve(self.lattice,kernel,mode = 'constant',cval =0)
        next_lattice = self.lattice.copy()
        for i in range(self.dimension_vertical):
            for j in range(self.dimension_horizontal):
                if self.lattice[i][j] == 1:
                    if neighbour_matrix[i][j] == 2 or neighbour_matrix[i][j] ==3:
                        pass
                    else:
                        next_lattice[i][j] = 0
                else:
                    if neighbour_matrix[i][j] == 3:
                        next_lattice[i][j] = 1
        self.lattice = next_lattice
                    

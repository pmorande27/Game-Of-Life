from Game import Game
import matplotlib.pyplot as plt
import numpy as np
from animate import Animation
import patterns


def main():
    pattern = patterns.get_patern('patterns/Simkin Glider Gun.txt')      
    pattern = patterns.center_pattern(pattern,59,59)
    ani = Animation(pattern)
    ani.animation()
    


    
main()
from Game import Game
import matplotlib.pyplot as plt
import numpy as np
from animate import Animation
import patterns


def main():
    pattern = patterns.get_patern('patterns/MWWS Synthesis.txt')      
    pattern = patterns.center_pattern(pattern,20,100)
    ani = Animation(pattern)
    ani.animation_save(100, 'MWWS Synthesis')
    


    
main()
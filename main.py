from Game import Game
import matplotlib.pyplot as plt
import numpy as np
from animate import Animation
import patterns


def main():
    pattern_name = 'Gosper Glider Gun'
    pattern = patterns.get_patern('patterns/'+pattern_name+'.txt')      
    pattern = patterns.center_pattern(pattern,100,100)
    ani = Animation(pattern)
    ani.animation_save(100, 'Hertz Oscillator')
    


    
main()
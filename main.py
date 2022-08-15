from Game import Game
import matplotlib.pyplot as plt
import numpy as np
from animate import Animation
import patterns


def main():
    options = ['Glider','Gosper Glider Gun','Hertz Oscillator','Kok\'s Galaxy','MWWS Synthesis','MWWS','pulsar','sailboat','Simkin Glider Gun']
    '''
    for pattern_name in options:
        pattern = patterns.get_patern('patterns/'+pattern_name+'.txt')      
        pattern = patterns.center_pattern(pattern,100,100)
        ani = Animation(pattern)
        ani.animation_save(300, pattern_name)
    '''
    pattern_name = 'Spider'
    pattern = patterns.get_patern('patterns/'+pattern_name+'.txt')      
    pattern = patterns.center_pattern(pattern,100,100)
    ani = Animation(pattern)
    ani.animation_save(300, pattern_name)

    


    
main()
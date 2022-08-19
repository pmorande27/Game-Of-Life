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
    '''
    pattern_name = 'Spider'
    pattern = patterns.get_patern('patterns/'+pattern_name+'.txt')      
    pattern = patterns.center_pattern(pattern,100,100)
    ani = Animation(pattern)
    ani.animation_save(300, pattern_name)
    '''
    '''
    for pattern_name in options:
        pattern = patterns.get_patern('patterns/'+pattern_name+'.txt') 
        pattern = patterns.center_pattern(pattern,100,100)
        plt.imshow(pattern, cmap='Greys')
        plt.savefig('results/Pictures/'+pattern_name+'_pattern.png')
    '''
    pattern_name = 'Block'
    pattern = patterns.get_patern('patterns/'+pattern_name+'.txt') 
    pattern = patterns.center_pattern(pattern,10,10)
    plt.imshow(pattern, cmap='Greys')
    plt.savefig('results/Pictures/'+pattern_name+'_pattern.png')
    

    


    
main()
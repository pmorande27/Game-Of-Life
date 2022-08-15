from Game import Game
import matplotlib.pyplot as plt
import numpy as np
from animate import Animation
def create_glider(n_x,n_y):
    pattern = np.zeros((n_x,n_y))
    if n_x < 3 or n_y < 3:
        raise ValueError()   
    pattern[0][2] = 1
    pattern[1][0] = 1
    pattern[1][2] = 1
    pattern[2][1] = 1
    pattern[2][2] = 1
    return pattern
def center_pattern(initial,n_vertical,n_horizontal):
    if n_vertical < len(initial) or n_horizontal < len(initial[0]):
        raise ValueError()
    vertical,horizontal = (len(initial),len(initial[0]))
    copy = initial.copy()
    diference_vertical = n_vertical-vertical
    diference_horizontal = n_horizontal -horizontal
    hor_left,hor_right = (diference_horizontal//2,diference_horizontal//2 +diference_horizontal%2)
    ver_top,ver_bottom = (diference_vertical//2,diference_vertical//2 +diference_vertical%2)
    for i in range(vertical):
        copy[i] = [0 for j in range(hor_left)]+copy[i] + [0 for j in range(hor_right)]
    for j in range(ver_bottom):
        copy = copy +[[0 for l in range(n_horizontal)]]
    for k in range(ver_top):
        copy =[[0 for l in range(n_horizontal)]]+ copy
    return np.array(copy)


def create_cloverleaf(n_vertical,n_horizontal):
    initial = [ [0,0,0,1,0,1,0,0,0],
                [0,1,1,1,0,1,1,1,0],
                [1,0,0,0,1,0,0,0,1],
                [1,0,1,0,0,0,1,0,1],
                [0,1,1,0,1,0,1,1,0],
                [0,0,0,0,0,0,0,0,0],
                [0,1,1,0,1,0,1,1,0],
                [1,0,1,0,0,0,1,0,1],
                [1,0,0,0,1,0,0,0,1],
                [0,1,1,1,0,1,1,1,0],
                [0,0,0,1,0,1,0,0,0]]
    return center_pattern(initial,n_vertical,n_horizontal)


def create_R_pentomino(n_vertical,n_horizontal):
    return center_pattern([[0,1,1],[1,1,0],[0,1,0]],200,200)

def get_patern(textfile):
    file = open(textfile,'r')
    lines = file.readlines()
    print(lines)
    file.close()
    for j in range(len(lines)):
        lines[j] = lines[j].strip()
        lines[j] = lines[j].replace('O','1')
        lines[j] = lines[j].replace('.','0')
        lines[j] = [int(x) for x in lines[j]]
    return lines



def main():
    pattern = get_patern('patterns/Gosper Glider Gun.txt')
    print(pattern)
            
    pattern = create_R_pentomino(150,150)
    print(pattern)
    ani = Animation(pattern)
    ani.animation()
    


    
main()
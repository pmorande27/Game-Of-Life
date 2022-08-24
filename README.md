# Game-Of-Life
## Introduction
This project uses python to simulate the famous Game of Life, designed by John Conway in 1970. This zero-player game is the perfect example of a cellular atutomaton (which have applications in Physics, Biology and microstructure modelling).
The game consists in a grid of cells which can be alive or dead, the status of the grid is updated each generation applying a simple set of rules:
1. If the cell is alive it will stay alive if it has either 2 or 3 alive neighbours.
2. If the cell is dead it will become alive if it has exactly 3 alive neighbours mimicking reproduction.
3. If none of the other rules apply the cell will stay/become dead.
This simple set of rules leads to astonishing results even with simple initial patterns.

## Patterns
This section outlines some example initial patterns that demonstrate the complexity of the Game of Life
### Still life
These initial patterns always remain without change
1. Block


![](results/Pictures/Block_pattern.png?raw=true "Block")

### Oscillators
These patterns return to their initial configurations after a set number of generations.
1. Pulsar

![](results/Pictures/pulsar_pattern.png?raw=true "Pulsar")

### Spaceships
These patterns traverse through the grid, they are moving patterns. Each of them with a different speed

1. Glider

![](results/Pictures/Glider_Pattern.png?raw=true "Glider")

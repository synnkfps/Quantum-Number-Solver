## Quantum Number Solver
Quantum number solver in Python (for my homework and my exam)

### Logic
```py
n = the number (e.g: 3)
l = the layer (e.g: 2 | 3D)
m = the position (from -l to +l) 
    |-->( e.g: -2 = [-2 | -1 | 0 | +1 | +2] )
    |--> Given -1: going to run all the way to -1, using S (spin)

s = spin/how to find the atom (+1/2 or -1/2 | e.g = +1/2 = 1)

if m = -1 and s = +1/2:
    This is our table:
    [-2 | -1 | 0 | +1 | +2]
           ^-- is where we want to go but using the + (plus) way
           ^-- plus way is the default starting found method

    [^  | ^  |   |   |   ]
    ^-----^----- both are up arrows because we are using the + (plus) way (up arrow)
    ^-----------> now its just count how much arrows there are!

    Our Valence Layer / Valence Electron / Valence Shell is 3D²

3D2 is our last layer! cool, right?!  
```

# Logic
'''
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
'''

n = int(input('Enter the n: '))
l = int(input('Enter the l: '))
m = int(input('Enter the m: '))
s = input('Enter the s: ')

# Rules
if m > l:
    print('The magnetic number cannot be greater than the layer (e.g: L=2 (d) M=3)')

definitions = {'S':0, 'P':1, 'D':2, 'F': 3}

chem = str(n)

for i in definitions:
    if definitions[i] == l:
        chem += i

scheme = []
for i in range((definitions[chem[-1]]*2)+1):
    scheme.append([])

ways = True

if str(m)[0] == '-': ways = False 
else: ways = True

pos = 0

# ways = True = M is in plus way
# ways = False = M is in negative way

if ways and s == '+1/2':
    print('is +1/2')
    for i in scheme:
        if pos == (m*2)+2:
            break
        i.append(1)
        pos += 1

if ways and s == '-1/2':
    # todo

if not ways and s == '+1/2':
    # todo

if not ways and s == '-1/2':
    # todo
        
    
            
print(chem, scheme)

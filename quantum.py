# Logic
# [ -2 | -1 | 0 | +1 | +2 ]

n = int(input('Enter the n: '))
l = int(input('Enter the l: '))
m = int(input('Enter the m: '))
s = input('Enter the s: ')

# Rules
if m > l:
    print('The magnetic number cannot be greater than the layer (e.g: L=2 (d) M=3)')

# S supports 2 | P supports 6 | D supports 10 | F supports 14
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
    for i in scheme:
        if pos == (m*2)+2:
            break
        i.append(1)
        pos += 1

if ways and s == '-1/2':
    for i in scheme:
        i.append(1)
    else:
        for i in scheme:
            if pos == (m*2)+2:
                break 
            i[0] += 1
            pos += 1

if not ways and s == '+1/2':
    for i in scheme:
        if pos == int(str(m)[1])+1:
            break 
        i.append(1)
        pos += 1

if not ways and s == '-1/2':
    for i in scheme:
        i.append(1)
    else:
        for i in scheme:
            if pos == (int(str(m)[1])*2):
                break 
            i[0] += 1
            pos += 1
              
#print(chem, scheme)

total = 0
for i in scheme:
    total += i[0]

chem += str(total)
print(chem)

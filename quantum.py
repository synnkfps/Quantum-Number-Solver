# Logic
# [ -2 | -1 | 0 | +1 | +2 ]

superscript = {0:'⁰', 1:'¹', 2:'²', 3:'³', 4:'⁴', 5:'⁵', 6:'⁶', 7:'⁷', 8:'⁸', 9:'⁹'}

n = int(input('Enter the n: '))
l = int(input('Enter the l: '))
m = int(input('Enter the m: '))
s = input('Enter the s: ')

# Rules
if m > l:
    print('The magnetic number cannot be greater than the layer (e.g: L=2 (d) M=3)')

# S supports 2 | P supports 6 | D supports 10 | F supports 14
definitions = {'S':0, 'P':1, 'D':2, 'F': 3}

shell = str(n)

for i in definitions:
    if definitions[i] == l:
        shell += i

table = []
for i in range((definitions[shell[-1]]*2)+1):
    table.append([])

ways = True

if str(m)[0] == '-': ways = False 
else: ways = True

pos = 0

# ways = True = M is in plus way
# ways = False = M is in negative way

if ways and (s == '+1/2' or s == '1/2'):
    for i in table:
        if pos == (m*2)+2:
            break
        i.append(1)
        pos += 1

if ways and s == '-1/2':
    for i in table:
        i.append(1)

    for i in table:
        if pos == (m*2)+2:
            break 
        i[0] += 1
        pos += 1

if not ways and (s == '+1/2' or s == '1/2'):
    mid = (int(len(table)/2))
    for i in table:
        i.append(1)
        if pos == (mid - int(str(m)[1])):
            break
        pos += 1

if not ways and s == '-1/2':
    for i in table:
        i.append(1)
    
    for i in table:
        if pos == (int(str(m)[1])*2):
            break 
        i[0] += 1
        pos += 1

total = 0
for i in table:
    print(i)
    if not not i:
        total += i[0]

for i in str(total):
    shell += superscript[int(i)]

#print(shell)
print("\t"*int(len(table)/3) + f'{shell}')

# ⇅, ↑
for i in table:
    if not not i:
        if i[0] == 2:
            i[0] = '⇅'

        if i[0] == 1:
            i[0] = '↑'

print('[ ' + str(table).replace(', ', ' | ').replace('\'','').replace('[','').replace(']','') + ' ]')

# Author: SynnK
# Date: 09/13/2022
# 11:29 AM

# Superscript / small numbers
superscript = {0:'⁰', 1:'¹', 2:'²', 3:'³', 4:'⁴', 5:'⁵', 6:'⁶', 7:'⁷', 8:'⁸', 9:'⁹'}

# Ask n l m s
# s is string because of the +1/2 or -1/2
n = int(input('Enter the n: '))
l = int(input('Enter the l: '))
m = int(input('Enter the m: '))
s = input('Enter the s: ')

# Rules
if m > l:
    print('The magnetic number cannot be greater than the layer (e.g: L=2 (d) M=3)')
 
if s != '-1/2':
    if s != '+1/2':
        print(f'The SPIN is wrong, only +1/2 and -1/2 is accepted! {s} is not valid.')

# S supports 2 | P supports 6 | D supports 10 | F supports 14
# (0*2+1)*2    | (1*2+1)*2    | (2*2+1)*2     | (3*2+1)*2
definitions = {'S':0, 'P':1, 'D':2, 'F': 3}

shell = str(n)

# Add the equivalent of the number in l (0=s, 1=p, 2=d, f=3)
for i in definitions:
    if definitions[i] == l:
        shell += i

# Create an empty table
# then setting its size to the layer*2+1 (so we have an middle block)
table = []
for i in range((definitions[shell[-1]]*2)+1):
    table.append([])

# ways System
# defines if its m is negative or positive
ways = True

if str(m)[0] == '-': ways = False 
else: ways = True

# ways = True = M is in plus way
# ways = False = M is in negative way

# Position to run
# the main part of the system, breaks at certain points
pos = 0

# Trigonometry

# + and +
if ways and (s == '+1/2' or s == '1/2'):
    for i in table:
        if pos == (m*2)+2:
            break
        i.append(1)
        pos += 1

# + and -
if ways and s == '-1/2':
    for i in table:i.append(1) # fill the table with 1's
    for i in table:
        if pos == (m*2)+2:
            break 
        i[0] += 1
        pos += 1

# - and +
if not ways and (s == '+1/2' or s == '1/2'):
    mid = (int(len(table)/2))
    for i in table:
        i.append(1)
        if pos == (mid - int(str(m)[1])):
            break
        pos += 1

# - and -
if not ways and s == '-1/2':
    mid = (int(len(table)/2))
    for i in table: i.append(1) # fill the table with 1's
    
    for i in table:
        if pos == (mid - int(str(m)[1])+1):
            break 
        i[0] += 1
        pos += 1

# Sum all the numbers of the table
total = 0
for i in table:
    # only if its not empty
    if not not i:
        total += i[0]

# Convert to superscript
for i in str(total):
    shell += superscript[int(i)]

# Telling the user the text within a space of the middle of the length of the string (of of of)
print(" "*int(len(table)*1.6) + f'{shell}')

# ⇅, ↑
# Replacing with the arrows
for i in table:
    if not not i:
        if i[0] == 2:
            i[0] = '⇅'

        if i[0] == 1:
            i[0] = '↑'

# Formatting the output
print('[ ' + str(table).replace(', ', ' | ').replace('\'','').replace('[','').replace(']','') + ' ]')

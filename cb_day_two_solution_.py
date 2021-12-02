import numpy as np

with open('puzzle.txt') as f:
    input = [tuple(i.strip('\n').split(' ')) for i in f.readlines()]
    input = [(x, int(i)) for x,i in input]
''' part 1'''
print(np.prod(np.sum([(i,0) if x =='forward' else (0,-i) if x =='up' else (0,i) for x,i in input ], axis=0)))

'''part 2'''

depth = 0
aim = 0
horizontal =0
for x,i in input:
    if x == 'forward':
        horizontal += i
        depth += aim*i
    elif x == 'up':
        aim -=i
    else:
        aim +=i
print(horizontal*depth)

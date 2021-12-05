from collections import Counter
import itertools
import numpy as np
with open('puzzle.txt') as f:
    nums = [(i.strip('\n').split(' -> ') )for i in f.readlines()]
    nums = [[eval(i[0]),eval(i[1])] for i in nums]
'''part 1'''
counter = Counter()
for i in nums:

    if i[0][0] == i[1][0]: #horizontal
        if i[0][1] > i[1][1]:
            counter.update(list(itertools.product([i[0][0]],range(i[1][1], i[0][1]+1))))
        else:
            counter.update(list(itertools.product([i[0][0]],range(i[0][1], i[1][1]+1))))

    elif i[0][1] == i[1][1]: #vertical
        if i[0][0] > i[1][0]:
            counter.update(list(itertools.product(range(i[1][0], i[0][0]+1),[i[0][1]])))
        else:
            counter.update(list(itertools.product(range(i[0][0], i[1][0]+1),[i[0][1]])))
    else:
        continue

print(len([i for i in counter.keys() if counter[i] > 1]))

'''part 2'''
counter = Counter()
for i in nums:

    if i[0][0] == i[1][0]: #horizontal
        if i[0][1] > i[1][1]:
            counter.update(list(itertools.product([i[0][0]],range(i[1][1], i[0][1]+1))))
        else:
            counter.update(list(itertools.product([i[0][0]],range(i[0][1], i[1][1]+1))))

    elif i[0][1] == i[1][1]: # vertical
        if i[0][0] > i[1][0]:
            counter.update(list(itertools.product(range(i[1][0], i[0][0]+1),[i[0][1]])))
        else:
            counter.update(list(itertools.product(range(i[0][0], i[1][0]+1),[i[0][1]])))

    elif i[0][0] < i[1][0] and i[0][1] < i[1][1]: # bottom right dir
        counter.update([tuple(i[0] + np.multiply((1,1),z)) for z in range(0, (abs(i[1][0]-i[0][0])+1))])

    elif i[0][0] > i[1][0] and i[0][1] < i[1][1]: # bottom left dir
        counter.update([tuple(i[0] +np.multiply((-1,1),z)) for z in range(0, (abs(i[1][0]-i[0][0])+1))])

    elif i[0][0] < i[1][0] and i[0][1] > i[1][1]: # up right dir
        counter.update([tuple(i[0] +np.multiply((1,-1),z)) for z in range(0, (abs(i[1][0]-i[0][0])+1))])

    else: # up left dir 
        counter.update([tuple(i[0] +np.multiply((-1,-1),z)) for z in range(0, (abs(i[1][0]-i[0][0])+1))])

print(len([i for i in counter.keys() if counter[i] > 1]))

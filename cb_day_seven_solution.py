import numpy as np
with open(r"puzzle.txt") as f:
    s = [int(i.strip('\n')) for i in f.read().split(',')]
    
'''part1'''

print(sum([abs(np.median(s) - i) for i in s]))

'''part2'''

center = round(np.mean(s))-1 # round down to nearest int or round up. round down worked for my puzzle
fuel = sum([sum(range(1,(abs(i-center)+1))) for i in s])
    
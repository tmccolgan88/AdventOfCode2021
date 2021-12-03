from collections import Counter
with open('puzzle.txt') as f:
    input = [i.strip('\n') for i in f.readlines()]
'''part 1'''
counters = []
for i in range(0,len(input[0])):
    counters.append(Counter([x[i] for x in input]))
    
gamma = int(''.join(counter.most_common(1)[0][0] for counter in counters),2)
epsilon = int(''.join(counter.most_common()[-1][0] for counter in counters),2)

print(gamma*epsilon)

'''part 2'''

oxygen = input.copy()
idx =0
while len(oxygen) != 1:
    if idx == len(oxygen[0])+1:
        break
    num = sorted(Counter([x[idx] for x in oxygen]).most_common(), key=lambda x: (x[1], x[0]), reverse=True)[0][0]
    oxygen = [x for x in oxygen if  x[idx] == num]
    idx+=1

co2 = input.copy()
idx =0
while len(co2) != 1:
    if idx == len(oxygen[0])+1:
        break
    num = sorted(Counter([x[idx] for x in co2]).most_common(), key=lambda x: (x[1], x[0]), reverse=False)[0][0]
    co2 = [x for x in co2 if  x[idx] == num]
    idx+=1

print(int(co2[0],2)*int(oxygen[0],2))
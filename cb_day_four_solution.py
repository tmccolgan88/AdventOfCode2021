import numpy as np
lines = len(open('puzzle.txt').readlines(  ))

with open('puzzle.txt') as f:
    nums = f.readline().split(',')
    nums = [int(i.strip('\n')) for i in nums]
    boards = []
    count = 0
    while lines-1 >= count:
        f.readline()
        try:
            temp = []
            for i in range(0,5):
                temp_nums = f.readline().split(' ')
                temp.extend([int(i.strip('\n')) for i in temp_nums if i != '' ])
                count+=1
            boards.append(np.array(temp).reshape(-1,5))

        except:
            print('except block')
            print(temp)
            print(np.array(temp).reshape(-1,5))
            break
boards = boards[0:100]
'''part 1'''
def find_winner():
    for i in nums:
        for x in range(0,len(boards)):
            boards[x] = np.where(boards[x] ==i,0, boards[x])
            if 0 in np.sum(boards[x], axis=0) or 0 in np.sum(boards[x], axis=1):
                print(np.sum(boards[x])*i)
                return 

find_winner()

'''part 2'''
def find_last_winner():
    winners = []
    scores = []
    for i in nums:
        for x in range(0,len(boards)):
            boards[x] = np.where(boards[x] ==i,1000, boards[x])
            if 5000 in np.sum(boards[x], axis=0) or 5000 in np.sum(boards[x], axis=1):
                if x not in winners:
                    winners.append(x)
                    scores.append(np.sum(np.where(boards[x] ==1000,0, boards[x]))*i)
    print(scores[-1])
    return 

find_last_winner()


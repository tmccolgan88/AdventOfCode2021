with open('puzzle.txt') as f:
    input = [i.strip('\n').split(' ') for i in f.readlines()]
 
# print(input[0][-4:])
# print(input[0][0:-5])

def square_of_numbers(num):
    if len(num) in set([2,3,4,7]):
        return 1
    else:
        return 0
# 2,4,3,7

print(sum([ sum(map(square_of_numbers,input[i][-4:])) for i in range(0,len(input)) ]))
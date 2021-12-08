with open('puzzle.txt') as f:
    input = [i.strip('\n').split(' ') for i in f.readlines()]
 
# print(input[0][-4:])
# print(input[0][0:-5])

'''part 1'''
def len_num(num):
    if len(num) in set([2,3,4,7]):
        return 1
    else:
        return 0
# 2,4,3,7

print(sum([ sum(map(len_num,input[i][-4:])) for i in range(0,len(input)) ]))

'''part2'''

def find_len(num):
    if len(num) ==4:
        return (num,4)
    elif len(num) ==2:
        return (num,1)
    elif len(num) ==7:
        return (num,8)
    elif len(num) ==3:
        return(num,7)
    else:
        return(num,'?')
# 2,4,3,7
ls = [list(map(find_len,input[i][0:-5])) for i in range(len(input)) ]

def get_decode_dict(line, inp):
    new_dict = {}
    i = line
    for k in i:
        #if len(k) == 6 & intersect1 2 time, & intersect4 3 time*
        key =''.join(sorted(k[0]))
        new_dict[k[1]] = key

    for k in i:
        if (len(k[0]) == 6) and len(set(k[0]).intersection(set(new_dict[1]))) == 2 and len(set(k[0]).intersection(set(new_dict[4]))) == 3:
            new_dict[0] = ''.join(sorted(k[0]))
        elif (len(k[0]) == 5) and len(set(k[0]).intersection(set(new_dict[4]))) == 2:
            new_dict[2] = ''.join(sorted(k[0]))
        elif (len(k[0]) == 6) and len(set(k[0]).intersection(set(new_dict[1]))) == 1:
            new_dict[6] = ''.join(sorted(k[0]))
        elif (len(k[0]) == 6) and len(set(k[0]).intersection(set(new_dict[1]))) == 2 and len(set(k[0]).intersection(set(new_dict[4]))) == 4:
            new_dict[9] = ''.join(sorted(k[0]))

    for k in i:

        if (len(k[0]) == 5) and len(set(k[0]).intersection(set(new_dict[2]))) == 3 and len(set(k[0]).intersection(set(new_dict[4]))) == 3:
            new_dict[5] = ''.join(sorted(k[0]))    
        elif (len(k[0]) == 5) and len(set(k[0]).intersection(set(new_dict[2]))) == 4 and len(set(k[0]).intersection(set(new_dict[4]))) == 3:
            new_dict[3] = ''.join(sorted(k[0]))

    decode = {v:k for k,v in new_dict.items() if k != '?'}

    return [decode[''.join(sorted(i))] for i in inp[-4:]]



final_code = []
for i in [get_decode_dict(ls[i], input[i]) for i in range(len(ls))]:
    strings = [str(integer) for integer in i]
    final_code.append(int("". join(strings)))

print(sum(final_code))
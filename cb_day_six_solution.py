with open('puzzle.txt') as f:
    s = f.read().split(',')
    s = [int(i.strip('\n')) for i in s]

from collections import Counter

'''part 1'''
def find_fish(start, days): # can also use np here
    fish_ids = (i for i in range(len(start),1000000000000000000000))
    fish_dict = {k:v for k,v in zip(range(0,len(start)),start)}
    for day in range(0,days):
        fish_dict.values()
        for key in list(fish_dict.keys()):
            fish_dict[key] -= 1
            if fish_dict[key] ==-1:
                fish_dict[key] = 6
                fish_dict[next(fish_ids)] = 8
            
    return len(fish_dict.keys())

print(find_fish(s, 80))

'''part 2'''
def find_fishes_now(start, days):
    fish_dict = Counter(start)
    for day in range(0,days):
        fish_dict = {k-1:v for k,v in fish_dict.items()}
        try: # if no key 6 still add key 8. used a lazy method here. would have been better to use defaultdict or intialize range(0,8)
            try:# if key 6 exists
                fish_dict[6] = fish_dict[6] + fish_dict[-1] 
                
            except:
                fish_dict[6] = fish_dict[-1]
            fish_dict[8] = fish_dict[-1]
            fish_dict.pop(-1)
        except:
            pass
    return sum(fish_dict.values())

print(find_fishes_now(s,256))
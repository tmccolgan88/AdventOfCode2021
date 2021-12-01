'''solution one using pandas'''

import pandas as pd

loaded = pd.read_csv('day_1_puzzle.txt', sep='\n', header=None)
diff = loaded.diff()
count = len(diff[diff[0] > 0])
#print(count)


'''solution two using pandas'''
loaded['second'] = loaded[0].shift(1)
loaded['third'] = loaded[0].shift(2)
loaded['sliding_window_three'] = loaded['second'] + loaded[0] + loaded['third']
loaded['final_diff'] = loaded['sliding_window_three'].diff()
part_two_count = len(loaded[loaded['final_diff'] > 0])

print(part_two_count)
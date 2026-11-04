# the behaviour of operators is NOT fixed, it's dynamic

print(1 + 1)            # 2
print('he' + 'llo')     # hello
print([1] + [2])        # [1, 2]

import datetime as dt 

date1 = dt.date(2026, 11, 4)
date2 = dt.date(1066, 10, 15)
print(date1 - date2)


import pathlib

path1 = pathlib.Path('home')
path2 = pathlib.Path('user1')
path3 = path1 / path2
print(path3)
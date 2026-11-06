# slicing: to make a copy of a subset of an indexed container 
# three numbers are needed:
# 1. starting index; incl.; default = 0
# 2. ending index; excl.; default = length of the container
# 3. step; default = 1

#           0123456789
greeting = 'Hello Dave'

slice1 = greeting[0:5:1]        # 'Hello'
slice2 = greeting[:5:]          # 'Hello'
slice3 = greeting[::2]          # 'HloDv'

print(greeting)
# see data_types.py for str, list, dict 

# tuple: an immutable list 
match = ('West Brom', 1, 'Southampton', 1)

home_team = match[0]
# match[3] = 2 

# ---

# set: like a dict but with no values
unique_numbers = {1, 2, 2, 3, 3, 3}
print(unique_numbers)

nums = [1, 2, 2, 3, 3, 3]
nums = set(nums)
print(nums)
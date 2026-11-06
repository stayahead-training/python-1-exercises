# object: a group of related variables (attributes) and functions (methods)
# EVERYTHING in Python is an object 
# we access an object's members via the dot notation 
# object.attribute or object.method()

# num is a variable
# 13 is an int object
num = 13

ones = num.bit_count()

# ---

# greeting is a variable
# 'Hello' is a str object
greeting = 'Hello'

num_of_ls = greeting.count('l')
greeting = greeting.upper()
print(greeting)

# ---

# nums is a variable
# [1, 2, 3] is a list object
nums = [1, 2, 3]

nums.append(4)
print(nums)

# ---

# coords is a variable
# {...} is a dict object
coords = {'x': 17, 'y': 11, 'z': 5}

for value in coords.values():
    print(value)
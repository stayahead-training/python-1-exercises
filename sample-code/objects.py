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

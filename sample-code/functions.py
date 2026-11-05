# function: some code stored in memory 
# why? reuse/avoid duplication; readability
# x % 2 == 1 # or...
# is_odd(x)

# def is a keyword used to declare a function
# parameter: a name for data that a function needs to do its work 
def is_odd(num):
    # the return keyword must precede the output value 
    # you can only return one thing but that thing can be anything
    return num % 2 == 1


def increment_all(nums):
    for index in range(len(nums)):
        nums[index] += 1


# type hint/annotation: type info added to a variable/parameter
# form : data_type

x: int = 1

# dict is a generic type; we can add the key and value types in []
# the return type is added with the -> but is redundant here
def full_name(user: dict[str, str]) -> str:
    return user['fname'] + ' ' + user['lname']

# you can create your own data types
# | is the bitwise or operator 
type Number = int | float
type Strings = list[str]
type User = dict[str, str]

# function params may have default values
def exp(num: int | float, pow=2):
    return num ** pow


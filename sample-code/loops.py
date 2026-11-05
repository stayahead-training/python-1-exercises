# loop/iterative statement: a statement in which the block is executed 0 or n times
# two types: while and for 

# while loop:
# 1. control variable
# 2. bool expression
# 3. update the control variable

count = 0

# the while keyword should be followed by a bool expression
while count < 3:
    print('Hello')
    count += 1

# for loops can only be used when iterating an iterable object 
# str, list, dict, tuple, set are all iterable

odd_nums = [1, 3, 5, 7, 9]
for num in odd_nums:
    print(num)

greeting = 'Hello'
for char in greeting:
    print(char)

book = {'title': 'Mr Strong', 'author': 'Hargreaves'}
for key in book:
    print(key)  

# the range function provides for arbitrary iterations in a for loop
for _ in range(3):
    print('Hello')

# ---

# infinite loops are required when you don't know how many iterations you need 
total = 0
while True:
    value = input('Enter the number to add or q to quit: ')
    if value == 'q':
        # the break keyword will terminate the loop immediately
        break 

    num = float(value)
    total += num 

print('Total:', total)
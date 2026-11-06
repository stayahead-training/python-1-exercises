# types of error:
# 1. syntax: mistake in the use of names, keywords, operators, symbols etc.
# 2. logic: mistake in the logic of the code
# 3. environmental: problems that result from things beyond your control 
# error handling SHOULD only apply to #3

# syntax error
# nums = [1. 2. 3]

# logic error
nums = [1, 2, 3]
# print(nums[3])

# environmental error 1
try:
    # the code here may produce an error
    file = open('errors.dat')
except:
    # the code here will only be executed IF an error occured above
    print('ERROR: The file cannot be read')
    exit()

for line in file:
    print(line)

# environmental error 2
while True:
    value = input('Enter a number between 1 and 10: ')
    try:
        num = int(value)
        break
    except:
        print('Invalid input - try again')



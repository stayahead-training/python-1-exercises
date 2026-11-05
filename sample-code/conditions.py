# condition: a statement in which 0 or 1 of n blocks is executed 

# the input function will return a str regardless of what the user enters 
temp = input('Enter the temperature: ')
temp = float(temp)

# if and elif are keywords that should be followed by a bool expression 
if temp < 10:
    # this block will ONLY be executed if the exp is True 
    # \ is the escape char in a str
    # \'  \"  \n (newline) \t (tabspace)  \\
    print('It\'s cold')

elif temp < 20:
    print('It\'s mild')

else:
    print('It\'s hot')
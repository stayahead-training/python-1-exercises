# expression: a statement that yields a new value in memory 

x = 7
y = 3

# x * y is an expression
# x and y are operands (may be variables or literals) 
# * is the multiplication operator
product = x * y

# the result of an expression may serve as the input to a function 
print(x * y)

# ---

# there are four categories of operator:
# 1. arithmetic: +  -  *  **  /  // (floor)  % (modulus/remainder)
# 2. relational: == (equal value)  !=  >  >=  <=  in (membership)  is (equal ref)
# 3. logical: and  or  not 
# 4. assignment: =  +=  -=  *=  /=

print(9 / 4)        # 2.25
print(9 // 4)       # 2 
print(9 % 4)        # 1

print(1 == 1)       # True
print(1 is 1)       # True
print([1] == [1])   # True
print([1] is [1])   # False

print('e' in 'Hello')       # True
print(2 in [1, 2, 3])       # True
print(1 in {'a': 1})        # False; when dealing with dicts we get keys by default, not values

# every value is truthy or falsey
# every value can be converted to bool
# falsey values: 0, 0.0, None, '', [], {}
# Python will automatically convet to bool in many situations

x = 5

if x:
    print('x is truthy')
else:
    print('x is falsey')


print(not x)

print(True and True)    # True
print(True and False)   # False

print('Hello' and 42)   # 42
print('' and 42)        # ''

print('Hello' or 42)    # 'Hello'
print('' or 42)         # 42

# ---

counter = 0

counter = counter + 1 # or...
counter += 1
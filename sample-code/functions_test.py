# the import keyword must be followed by a filename without ext.
import functions as fn

# you can import functions directly (no prefix needed)
# from functions import is_odd

# this is a function call/invocation
# 5 is an argument
result = fn.is_odd(5)
print(result)

print(fn.is_odd(5))

# NB: we pass refs to objects, not objects themselves
# Python doesn't pass data around
scores = [5, 2, 7]
fn.increment_all(scores)
print(scores)

print(fn.full_name({'fname': 'Dave', 'lname': 'Smith'}))

print(fn.exp(2, 2))
print(fn.exp(2))

# we can pass args in any order provided they're named
print(fn.exp(pow=4, num=2))
# there are seven builtin data types you MUST memorise: bool, int, float, None, str, list, dict

# bool
is_active = True 

# int
num_delegates = 10

# float
duration = 2.35

# None
empty = None

# str, list and dict are containers

# str
greeting = 'Hello'
greeting = "Hello"

# list
delegates = ['Anderson', 'Ayana', 'Diego']
delegates = [
    'Anderson', 
    'Ayana', 
    'Diego'
]

# dict
book = {'title': 'The Cat in the Hat', 'author': 'Dr. Seuss'}
book = {
    'title': 'The Cat in the Hat',
    'author': 'Dr. Seuss'
}

# each of str, list and dict are subscriptable 
# the elements in a container can be accessed using the [] notation 

print(greeting[0])
print(delegates[0])
print(book['title'])

# list and dicts are MUTABLE!
delegates[0] = 'Julien'
book['title'] = 'Fox in Socks'
# a book has a title, author, year (of publication), and is reviewed n times
# how might we store n books in memory, all referenced by one variable?

# version #1
books = [
    {'title': 'Book 1', 'author': 'Dave', 'year': 2026, 'reviews': ['I liked it', 'It was a great read']},
    {'title': 'Book 2', 'author': 'Sam', 'year': 2021, 'reviews': ['It was ok', 'Gave up after the first chapter']}
]

# print the title of the second book
print(books[1]['title'])

# print the last review of the first book
print(books[0]['reviews'][1])

# ---

# version #2
books = {
    'title': ['Book 1', 'Book 2'],
    'author': ['Dave', 'Sam'],
    'year': [2026, 2021],
    'reviews': [['I liked it', 'It was a great read'], ['It was ok', 'Gave up after the first chapter']]
}

# print the title of the second book
print(books['title'][1])

# print the last review of the first book
print(books['reviews'][0][1])
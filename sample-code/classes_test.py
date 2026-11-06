import classes as cls

# create a Rectangle object
rect1 = cls.Rectangle(7, 4)

# is it really a Rectangle?
print(type(rect1))

# print the Rectangle's width and length
print(rect1.width, 'x', rect1.length)

print(rect1.area())
rect1.width += 2
print(rect1.area()) 
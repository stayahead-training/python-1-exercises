# class: a spec of the attributes and methods that comprise objects of a given type 
# a class is a template/blueprint 
# every class is a data type 

# class is a keyword
# classes should be named PascalCase 
class Rectangle:

    # this method will be called by Pyhthon when we create a Rectangle object 
    def __init__(self, width, length):
        self.width = width
        self.length = length 

    def area(self):
        return self.width * self.length

    # TODO add two methods:
    # 1. perimeter
    # 2. scale
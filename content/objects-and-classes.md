<img src="https://github.com/stayahead-training/shared/blob/master/stayahead.png" />

# Objects and Classes Exercises

[<<< back](../README.md)

1. What is the point of objects?

    <details>
    <summary>Show me</summary>

    *Objects provide for the grouping of related data and the functions that operate on that data. Every thing in Python is an object.*
    </details>

2. Which of the following words best describe the thing on the left of the dot and the thing on the right?

    ```python
    team.name
    ```
 
    - Function
    - Attribute
    - Object
    - Field
    - Method
    - Property
    - Object reference
    - Container
    - Variable
    <br />
    <details>
    <summary>Show me</summary>

    - Object reference
    - Attribute
    </details>

3. Use Python in interactive/REPL mode to store the number `5` in memory such that it is accessible using the name `num`. Then call the object's `bit_length` method. Can you explain the output?

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> num = 5
    >>> num.bit_length()
    3
    >>> exit()
    ```
    </details>

4. Use Python in interactive/REPL mode to store the word `Hello` in memory such that it is accessible using the name `word`. Then call the object's `rfind` method with one argument - `l` (lower case L). Can you explain the output?

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> word = "Hello"
    >>> word.rfind("l")
    3
    >>> exit()
    ```
    </details>

5. Use Python in interactive/REPL mode to store the numbers `1`, `2`, and `3` in memory such that they are accessible using the name `nums`. Then call the object's `pop` method. Can you explain the output? And does the method mutate the object?

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> nums = [1, 2, 3]
    >>> nums.pop()
    3
    >>> exit()
    ```
    </details>

6. Use Python in interactive/REPL mode to store the tabular data given below in memory such that it is accessible using the name `result`. Then call the object's `get` method with two arguments - `"math_score"` and `-1`. Can you explain the output?

    |Name  |Reading score |Writing score |
    |------|--------------|--------------|
    |Peter |71            |63            |

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> result = {
    ... "name": "Peter",
    ... "reading_score": 71,
    ... "writing_score": 63
    ... }
    >>> result.get("math_score", -1)
    -1
    exit()
    ```
    </details>

7. Which built-in function lists the attributes and methods available on the referenced object?

    <details>
    <summary>Show me</summary>

    ```python
    dir
    ```
    </details>

8. Which **float** method is used to determine whether the number is whole?

9. Which **str** method is used to determine whether the string is comprised entirely of whitespace (spaces, newline characters, tab spaces etc.)?

10. Which **list** method is used to determine the frequency of a given value?

11. Which **dict** method is used to remove all key value pairs?

12. bool, int, float, and str methods always return something. list and dict methods don't. Why?

    <details>
    <summary>Show me</summary>
    <br />
    *bool, int, float, and str methods always return something because objects of those types are immutable. The referenced object cannot be modified so the methods must return something.*
    
    *list and dict methods don't always return something because object of those types are mutable. The methods may mutate the referenced object instead of/in addition to returning something.*
    </details>

13. Which does dunder stand for, and what purpose do dunder attributes and methods serve?

    <details>
    <summary>Show me</summary>
    <br />
    *Dunder stands for double underscore. Dunder attributes and methods (those named with two leading and two trailing underscores) are for internal use by Python and should not be accessed directly.*
    
    *Dunder methods provide the implementations for operators and builtin functions.*
    </details>

14. What are the values of `x` and `y` after the following code is executed, and why?

    ```python
    x = "Hello"
    y = x
    x += " world"
    ```

    <details>
    <summary>Show me</summary>
    <br />
    *`x` is `"Hello world"` and `y` is `"Hello"`.*

    *After the second line of code is executed, both `x` and `y` reference the same string object.* 
    
    *Strings are immutable, so the third line results in the creation of a new string object - `"Hello world"`, and `x` is updated to reference the new object.* 
    
    *`y` is unaffected by the change and still references the original string object - `"Hello"`.*
    </details>

15. What are the values of `x` and `y` after the following code is executed, and why?

    ```python
    x = ["Hello"]
    y = x
    x[0] += " world"
    ```

    <details>
    <summary>Show me</summary>
    <br />
    *`x` is `["Hello world"]` and `y` is `["Hello world"]`.*

    *After the second line of code is executed, both `x` and `y` reference the same list object.* 
    
    *Lists are mutable, so the third line updates the first (only) reference in the list object to reference a new string object - `"Hello world"`.* 
    
    *`y` is affected by the change because it references the same list object as does `x`. No new list object was created.*
    </details>

16. Use Python in interactive/REPL mode to declare two variables - `x` and `y`, each assigned the string `"Immutable"`. Then write some code to prove that there is only one string object in memory.

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> x = "Immutable"
    >>> y = "Immutable"
    >>> id(x)
    >>> id(y)
    >>> exit()
    ```
    </details>

17. In a script named <b>calculator.py</b> code a class named `Calculator`. Each Calculator should have a `total` and methods to add, subtract, multiply, and divide the given amount against the total. Each Calculator should also have an equals methods that returns and resets the total.

    <details>
    <summary>Show me</summary>

    ```python
    class Calculator:

        def __init__(self):
            self.total = 0

        def add(self, amount):
            self.total += amount

        def sub(self, amount):
            self.total -= amount

        def mul(self, amount):
            self.total *= amount

        def div(self, amount):
            self.total /= amount

        def equals(self):
            return_value = self.total
            self.total = 0
            return return_value
    ```
    </details>

18. In a script named <b>calculator_test.py</b> write some code to test your Calculator class.

19. To what does the method parameter conventionally named `self` refer?

    <details>
    <summary>Show me</summary>
    <br />
    *The method parameter conventionally named `self` refers to the current object.* 
    
    *Given the class exists before any object that is created from it, one cannot know how to reference said objects in advance. Python deals with this problem by automatically passing a reference to the object on which the method is called as the first argument to each of the methods. This is why the first parameter in each method is named self, but could, in fact, be named anything.*
    </details>

[<<< back](../README.md)
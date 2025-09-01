<img src="https://github.com/stayahead-training/shared/blob/master/stayahead.png" />

# Functions Exercises

[<<< back](../README.md)

1. Create two files, one named **my_functions.py** and the other named **my_functions_test.py**. Each of the functions described below should be defined in my_functions.py and tested in my_functions_test.py. Each function should be named as you see fit. **Note that one should not have to examine the body of a function to know what it does.**

2. Code a function that writes `Hello` to stdout.<details>
    <summary>Show me</summary>

    Function definition (in my_functions.py):

    ```python
    def print_hello():
        print("Hello")
    ```

    Function test (in my_functions_test.py):
    
    ```python
    import my_functions as mf
    
    mf.print_hello()
    ```
</details>

2. Code a function that writes `Hello [name]` to stdout where `[name]` is passed to the function as an argument.<details>
    <summary>Show me</summary>

    Function definition (in my_functions.py):

    ```python
    def print_hello_to(name):
        print("Hello", name)
    ```

    Function test (in my_functions_test.py):
    
    ```python
    import my_functions as mf
    
    mf.print_hello_to("Fred")

    some_name = "Fred"
    mf.print_hello_to(some_name)

    ```
</details>

3. Code a function that outputs (returns) `Goodbye [name]` where `[name]` is passed to the function as an argument.<details>
    <summary>Show me</summary>

    Function definition (in my_functions.py):

    ```python
    def goodbye_to(name):
        return "Goodbye " + name
    ```

    Function test (in my_functions_test.py):
    
    ```python
    import my_functions as mf
    
    print(mf.goodbye_to("Fred"))

    some_name = "Fred"
    print(mf.goodbye_to(some_name))

    ```
</details>

4. Code a function that returns the product of the two numbers given as arguments.<details>
    <summary>Show me</summary>

    Function definition (in my_functions.py):

    ```python
    def product(num1, num2):
        return num1 * num2
    ```

    Function test (in my_functions_test.py):
    
    ```python
    import my_functions as mf
    
    print(mf.product(5, 7))

    n1 = 5
    n2 = 7
    print(mf.product(n1, n2))
    ```
</details>

5. Code a function that returns the first element in the list given as an argument.<details>
    <summary>Show me</summary>

    Function definition (in my_functions.py):

    ```python
    def first_element(some_list):
        return some_list[0]
    ```

    Function test (in my_functions_test.py):
    
    ```python
    import my_functions as mf
    
    print(mf.first_element(["a", "b", "c"]))

    my_list = ["a", "b", "c"]
    print(mf.first_element(my_list))

    ```
</details>

6. Code a function that accepts a dict with `fname` and `lname` keys. It should print the first name and last name on one line with a space between each name.<details>
    <summary>Show me</summary>

    Function definition (in my_functions.py):

    ```python
    def print_full_name(dict_with_fname_and_lname_keys):
        print(dict_with_fname_and_lname_keys["fname"], dict_with_fname_and_lname_keys["lname"])
    ```

    Function test (in my_functions_test.py):
    
    ```python
    import my_functions as mf
    
    mf.print_full_name({"fname": "John", "lname": "Smith"})

    user = {"fname": "John", "lname": "Smith"}
    mf.print_full_name(user)

    ```
</details>

7. Modify the function you created for task 2 such that the name parameter is optional. If the caller does not pass a name the function should print `Hello Guest`.<details>
    <summary>Show me</summary>

    Function definition (in my_functions.py):

    ```python
    def print_hello_to(name="Guest"):
        print("Hello", name)
    ```

    Function test (in my_functions_test.py):
    
    ```python
    import my_functions as mf
    
    mf.print_hello_to("Fred")

    some_name = "Fred"
    mf.print_hello_to(some_name)

    mf.print_hello_to() # <!--
    ```
</details>

8. Code a function that accepts a number and an exponent as arguments and returns the number raised to the given power. Test it using keyword arguments, that is, call it such that the exponent is the first argument given and the number is the second.<details>
    <summary>Show me</summary>

    Function definition (in my_functions.py):

    ```python
    def to_the_power(number, exponent):
        return number ** exponent
    ```

    Function test (in my_functions_test.py):
    
    ```python
    import my_functions as mf
    
    print(mf.to_the_power(exponent=2, number=3))

    exp = 2
    num = 3
    print(mf.to_the_power(exponent=exp, number=num))
    ```
</details>

9. Code a function that increments by one a global variable named `counter`.<details>
    <summary>Show me</summary>

    Function definition (in my_functions.py):

    ```python
    counter = 10

    def increment_counter():
        global counter
        counter += 1
    ```

    Function test (in my_functions_test.py):
    
    ```python
    import my_functions as mf

    mf.increment_counter()
    print(mf.counter)
    ```
</details>

10. What is written to stdout by the following code?

    ```python
    num = 1
    def do_something():
        num = 10

    do_something()
    print(num)
    ```

11. What is written to stdout by the following code?

    ```python
    num = 1
    def do_something():
        print(num + 10)

    do_something()
    ```

12. What is written to stdout by the following code?

    ```python
    def do_something(num):
        if num == 0:
            return 0
        return num + do_something(num - 1)

    result = do_something(3)
    print(result)
    ```

[<<< back](../README.md)
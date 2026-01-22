<img src="https://github.com/stayahead-training/shared/blob/master/stayahead.png" />

# Exception Handling Exercises

[<<< back](../README.md)

1. What is output by the following lines of code?

    ```python
    def my_function():
        raise Exception()

    try:
        total = 1
        my_function()
        total += 1
    except:
        total += 1
    finally:
        total += 1

    print(total)
    ```

2. Copy the following code into a script named bad_user_input.py.

    ```python
    num = int(input("Enter a number: "))
    square = num ** 2
    print("The square of", num, "is", square)
    ```

    This script will raise an exception and crash if the user does not enter a valid number. Refactor it so that it does not crash under any circumstances. You should try to recover from bad user input.
    
    <details>
    <summary>Show me</summary>

    ```python
    while True:
        num = input("Enter a number: ")
        try:
            num = int(num)
            break
        except:
            print("That's not a valid number - try again")

    square = num ** 2
    print("The square of", num, "is", square)
    ```
    </details>

3. What is output by the following lines of code?

    ```python
    total = 0
    
    def f1():
        global total
        total += 1

    def f2():
        global total
        total += 2
        raise Exception()
        f1()

    def f3():
        global total
        total += 3
        f2()

    try:
        f3()
        total += 5
    except:
        total -= 1

    print(total)
    ```

[<<< back](../README.md)
<img src="https://github.com/stayahead-training/shared/blob/master/stayahead.png" />

# Conditions and Loops Exercises

[<<< back](../README.md)

1. Code a script named **thats_odd.py** that prompts the user to enter a number and writes to stdout either `Yes - it's odd!` or `No - that's even!` depending on the value of the number entered.

    <details>
    <summary>Show me</summary>

    ```python
    num = input("Enter a number: ")
    num = int(num)
    if num % 2:
        print("Yes - it's odd!")
    else:
        print("No - that's even!")
    ```
    </details>

2. Code a script named <b>generations.py</b> that prompts the user to enter the year in which he/she was born. The script should write to stdout the user's generation, e.g. Maturist (pre 1946) Baby Boomer (1946-1960), Gen X (1961-1980), Millenial (1981-1995), or Gen Z (post 1995).

    <details>
    <summary>Show me</summary>

    ```python
    year = input("Enter the year you were born: ")
    year = int(year)
    if year < 1946:
        print("Maturist")
    elif year < 1961:
        print("Baby Boomer")
    elif year < 1981:
        print("Gen X")
    elif year < 1996:
        print("Millenial")
    else:
        print("Gen Z")
    ```
    </details>

3. Code a script named **every_even_number_to.py** that prompts the user to enter a number and writes to stdout every even number from 0 to the number given. Use a while loop.

    <details>
    <summary>Show me</summary>

    ```python
    max_num = input("Enter a number: ")
    max_num = int(max_num)
    current_num = 0
    while current_num < max_num:
        print(current_num)
        current_num += 2
    ```
    </details>

4. Code a script named **adding_machine.py** that repeatedly prompts the user to enter a number until he/she enters `q` (for quit). The number entered in each iteration should be added to a total (initially 0) and the total should be written to stdout.

    <details>
    <summary>Show me</summary>

    ```python
    total = 0
    while True:
        value = input("Enter a number or q to quit: ")
        if value == "q":
            break
        else:
            value = float(value)
            total += value
            print(total)

    ```
    </details>

5. Refactor the task 3 code to use a for loop with the built-in `range` function instead of a while loop.

    <details>
    <summary>Show me</summary>

    ```python
    max_num = input("Enter a number: ")
    max_num = int(max_num)
    for num in range(0, max_num, 2):
        print(num)
    ```
    </details>

6. Code a script named **cube_it.py** that stores a list of numbers from 1-10 in memory and then writes to stdout the cube of each of number in the list.

    <details>
    <summary>Show me</summary>

    ```python
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in nums:
        print(num ** 3)
    ```
    </details>

7. Copy the list of dictionaries below into a script named <b>initials.py</b> and write the initials of each user to stdout.

    ```python
    users = [
        {"fname": "Tom", "lname": "Harrison"},
        {"fname": "Jane", "lname": "King"},
        {"fname": "Susan", "lname": "Johnson"},
        {"fname": "Mike", "lname": "Taylor"},
        {"fname": "Yanis", "lname": "Paulus"}
    ]
    ```
    
    <details>
    <summary>Show me</summary>

    ```python
    users = [
        {"fname": "Tom", "lname": "Harrison"},
        {"fname": "Jane", "lname": "King"},
        {"fname": "Susan", "lname": "Johnson"},
        {"fname": "Mike", "lname": "Taylor"},
        {"fname": "Yanis", "lname": "Paulus"}
    ]
    for user in users:
        print(user["fname"][0], user["lname"][0], sep="")
    ```
    </details>

8. What is written to stdout by the following code?

    ```python
    for num in range(5):
        if num == 3:
            continue
        print(num)
    ```

9. What is written to stdout by the following code?

    ```python
    total = 0
    for num in range(5):
        total += 1
        if num * 2 == 0:
            break
    else:
        total += 1

    print(total)
    ```

10. What is written to stdout by the following code?

    ```python
    num = 9
    total = 0
    while num > 0:
        if num % 3 != 0:
            break
        total += 1
        num -= 3
    else:
        total += 1
    
    print(total)
    ```

[<<< back](../README.md)
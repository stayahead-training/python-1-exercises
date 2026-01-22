<img src="https://github.com/stayahead-training/shared/blob/master/stayahead.png" />

# Operators and Expressions Exercises

[<<< back](../README.md)

1. What is the result of each of the following arithmetic expressions? Execute some/all of the expressions using Python in interactive/REPL mode if you have to. Be sure that you understand each result before moving on.

    - `2 / 4`
    - `2 / 0`
    - `0 / 3`
    - `7 / 2`
    - `7 % 2`
    - `7 // 2`
    - `2 ** 3`
    - `1 + 1.0`
    <br />

2. What is the result of each of the following relational expressions? Execute some/all of the expressions using Python in interactive/REPL mode if you have to. Be sure that you understand each result before moving on.

    - `1 == 1.0`
    - `1 != 1.0`
    - `7 >= 7`
    - `False < True`
    - `"o" in "world"`
    - `4 in [1, 2, 3]`
    - `4 not in [1, 2, 3]`
    - `1 is 1.0`
    <br />

3. Use Python in interactive/REPL mode to determine the truthiness/falsiness of each of the following values: `0`, `0.0`, `1`, `2`, `2.5`, `""`, `" "`, `"Hello"`, `[]`, `[1]`, `[1, 2, 3]`, `{}`, `{"a": 1}`, and `None`.

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> bool(0)
    False
    >>> bool(0.0)
    False
    >>> bool(1)
    True
    ...
    ```
    </details>

4. What is the result of each of the following logical expressions. Execute some/all of the expressions using Python in interactive/REPL mode if you have to. Be sure that you understand each result before moving on.

    - `True and True`
    - `True and False`
    - `False and True`
    - `True or True`
    - `True or False`
    - `False or True`
    <br />

5. Use Python in interactive/REPL mode to store the number `0` in memory such that it is accessible using the name `num`. Then use assignment operators change the value of num as follows:

    - add 5
    - subtract 2
    - multiply by 3
    - divide by 2

    Finally, have Python write the value of num to the screen.
    
    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> num = 0
    >>> num += 5
    >>> num -= 2
    >>> num *= 3
    >>> num /= 2
    >>> num
    4.5
    >>> exit()
    ```
    </details>

6. What is the result of each of the following compound expressions. Execute some/all of the expressions using Python in interactive/REPL mode if you have to. Be sure that you understand each result before moving on.

    - `2 + 3 * 4`
    - `(2 + 3) * 4`
    - `2 * 3 / 1.5`
    - `13 % 5 + 1`
    - `10 - 6 // 4`
    - `2 // 4 / 2`
    - `10 > 9 * 2`
    - `2 + 2 == 2`
    - `4 * 5 in [10, 20, 30]`
    - `5 > 2 ** 2 and not 1 - 5 % 2`

[<<< back](../README.md)
<img src="https://github.com/stayahead-training/shared/blob/master/stayahead.png" />

# Variables and Data Types Exercises

[<<< back](../README.md)

1. Categorise each of the following as either data or a name for some data stored in memory.

    - `"Hello"`
    - `age`
    - `4.99`
    - `'name'`
    - `77`
    - `True`
    - `fred`
    <br />
    <details>
    <summary>Show me</summary>
    
    - `"Hello"`: data; surrounded by quotes
    - `age`: name; no quotes; does not begin with a digit; is not a keyword
    - `4.99`: data; starts with a digit
    - `'name'`: data; surrounded by quotes
    - `77`: data; starts with a digit
    - `True`: data; is a keyword
    - `fred`: name; no quotes; does not begin with a digit; is not a keyword
    </details>

2. Use Python in interactive/REPL mode to store the number `5000` in memory such that it is accessible using the name `loan_amount`. Then compute 18% of the loan amount.

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> loan_amount = 5000
    >>> loan_amount * 0.18
    900.0
    >>> exit()
    ```
    </details>

3. Use Python in interactive/REPL mode to store the number `7.50` in memory such that it is accessible using the name `price`. Then compute the price reduced by 10%.

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> price = 7.50
    >>> price - price * 0.1
    6.75
    >>> exit()
    ```
    </details>

4. Use Python in interactive/REPL mode to store your name in memory such that it is accessible using the name `my_name`. Then have Python write the value of my_name to the screen.

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> my_name = "Stuart"
    >>> my_name
    'Stuart'
    >>> exit()
    ```
    </details>

5. Use Python in interactive/REPL mode to store the words `cup` and `board` in memory such that the first word is accessible using the name `first_word`, and the second word is accessible using the name `second_word`. Then have Python write the values of both names to the screen on one line. Note that the `+` operator may be used to concatenate (join) text data together.

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> first_word = "cup"
    >>> second_word = "board"
    >>> first_word + second_word
    'cupboard'
    >>> exit()
    ```
    </details>

6. Use Python in interactive/REPL mode to store the words `mea` and `culpa` in memory such that the first word is accessible using the name `first_word`, and the second word is accessible using the name `second_word`. Then have Python write the values of both names to the screen with a space in between.

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> first_word = "mea"
    >>> second_word = "culpa"
    >>> first_word + " " + second_word
    'mea cupla'
    >>> exit()
    ```
    </details>

7. Use Python in interactive/REPL mode to store the number `25` in memory such that it is accessible using the name `weeks`. Then compute the number of days in the given weeks. Finally, assign a new value to the name weeks - `32` - and compute again the number of days.

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> weeks = 25
    >>> weeks * 7
    175
    >>> weeks = 32
    >>> weeks * 7
    224
    >>> exit()
    ```
    </details>

NB: When using Python in interactive/REPL mode the result of each expression is automatically written to the screen, e.g.:

```
>>> 1 + 1
2
```

or...

```
>>> name = "Fred"
>>> name
'Fred'
```

But when executing a script with Python the result of each expression is **not** automatically written to the screen. To write a value to the screen when coding a script we must use the built-in `print` function, e.g.:

```python
print(1 + 1)
```

or...

```python
name = "Fred"
print(name)
```

8. Code a script named <b>rugby.py</b> that stores the number `3` in memory such that it is accessible using the name `tries`. Then compute the score and write to the screen (each try is worth 5 points). Execute the script using Python when you're done.

    <details>
    <summary>Show me</summary>

    File contents:

    ```python
    tries = 3
    print(tries * 5)
    ```

    Commands:
    ```
    $ python3 rugby.py
    15
    ```
    </details>

9. Extend the rugby script such that it also stores in memory the number of conversions (2) and the number of penalties (1). Each conversion is worth 2 points, and each penalty is worth 3 points. Refactor the code such that the score is the sum of the points scored for all tries, conversions, and penalties.

    <details>
    <summary>Show me</summary>

    File contents:

    ```python
    tries = 3
    conversions = 2
    penalties = 1
    print(tries * 5 + conversions * 2 + penalties * 3)
    ```

    Commands:

    ```
    $ python3 rugby.py
    22
    ```
    </details>

10. Which of the following are built-in Python data types?

    - `int`
    - `number`
    - `float`
    - `text`
    - `str`
    - `bool`
    - `boolean`
    <br />
    <details>
    <summary>Show me</summary>
    
    - `int`
    - `float`
    - `str`
    - `bool`
    </details>

11. Which of the following lines of code will write to the screen the data type of the name `x`?

    - `print(dir(x))`
    - `print(dt(x))`
    - `print(type(x))`
    - `print(data_type(x))`
    <br />
    <details>
    <summary>Show me</summary>

    - `print(type(x))`
    </details>

12. Use Python in interactive/REPL mode to store in memory the numbers `10`, `20`, and `30` in a list named `nums`. Then have Python write the second element in the list to the screen.

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> nums = [10, 20, 30]
    >>> nums[1]
    20
    >>> exit()
    ```
    </details>

13. Copy the code below into a script named <b>names.py</b> then add to it such that `['Tom', 'Dick', 'Harry']` is written to the screen when the script is executed.

    ```python
    names = ["Thomas", "Dick", "Harry"]
    # your code here
    print(names)
    ``` 
    
    <details>
    <summary>Show me</summary>

    File contents:

    ```python
    names = ["Thomas", "Dick", "Harry"]
    names[0] = "Tom"
    print(names)
    ```

    Commands:

    ```
    $ python3 names.py
    ['Tom', 'Dick', 'Harry']
    ```
    </details>

14. Use Python in interactive/REPL mode to store in memory a client's name - `John Smith` - and his email address - `jsmith@mail.com` - in a dictionary named `client`. Then have Python write the client's email address to the screen.

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> client = {"name": "John Smith", "email": "jsmith@mail.com"}
    >>> client["email"]
    'jsmith@mail.com'
    >>> exit()
    ```
    </details>

15. Copy the code below into a script named <b>football.py</b> then add to it to reflect the fact that Liverpool have scored. Execute the script when you're done.

    ```python
    football_match = {
        "home_team": "Chelsea",
        "away_team": "Liverpool",
        "home_team_score": 0,
        "away_team_score": 0
    }
    # your code here
    print(football_match)
    ```

    <details>
    <summary>Show me</summary>

    File contents:

    ```python
    football_match = {
        "home_team": "Chelsea",
        "away_team": "Liverpool",
        "home_team_score": 0,
        "away_team_score": 0
    }
    football_match["away_team_score"] = 1
    print(football_match)
    ```

    Commands:

    ```
    $ python3 football_match.py
    {'home_team': 'Chelsea', 'away_team': 'Liverpool', 'home_team_score': 0, 'away_team_score': 1}
    ```
    </details>

16. What is output by the following line of code?

    ```
    >>> int("123") + 1
    ```

    <details>
    <summary>Show me</summary>

    ```
    124
    ```
    </details>

17. What is output by the following line of code?

    ```
    >>> str(123) + "1"
    ```

    <details>
    <summary>Show me</summary>

    ```
    '1231'
    ```
    </details>

[<<< back](../README.md)
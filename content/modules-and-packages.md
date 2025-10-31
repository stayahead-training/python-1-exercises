<img src="https://github.com/stayahead-training/shared/blob/master/stayahead.png" />

# Modules and Packages Exercises

[<<< back](../README.md)

Note that some of these tasks will require you to do some research into standard library modules.

1. Using the standard library module, `datetime`, create a module containing a function that returns the date a week from today. Then code a script that tests your module.<details>
    <summary>Show me</summary>

    ```python
    # my_date_functions.py
    def a_week_from_today():
        import datetime as dt
        today = dt.date.today()
        delta = dt.timedelta(days=7)
        return today + delta

    # my_date_functions_test.py
    import my_date_functions as mdf
    assert str(mdf.a_week_from_today()) == ...
    ```
</details>

2. Using the standard library module, `turtle`, create a module containing a function that accepts a turtle and has it draw a square of the given size. Then code a script that tests your module.<details>
    <summary>Show me</summary>

    ```python
    # my_turtle_functions.py
    def draw_square(turtle, size):
        for _ in range(4):
            turtle.forward(size)
            turtle.right(90)

    # my_turtle_functions_test.py
    import turtle
    import my_turtle_functions as mtf
    my_turtle = turtle.Turtle()
    mtf.draw_square(my_turtle, 100)
    ```
</details>

3. What command would one run to install the 3rd party library `requests`?<details>
    <summary>Show me</summary>

    ```
    $ pip3 install requests
    ```
</details>

4. What does the `__pycache__` directory contain and what purpose does it serve?<details>
    <summary>Show me</summary>

   *The `__pycache__` directory contains a cache of bytecode files (compiled Python source code) - one for each imported module. These files serve to speed up the loading of imported modules on subsequent executions of the script.*
</details>

5. Use Python in interactive/REPL mode to execute the following code:

    ```python
    import sys
    for path in sys.path:
        print(path)
    ```

    Now create a module containing a trivial function and move it into one of the paths listed by the code you executed previously. Then code a script and verify your module can be imported.

6. Which of the following do you think is the best way to import a module and why?

    - `import my_module`
    - `from my_module import *`
    - `import my_module as mm`
    - `from my_module import my_function`

7. Under what circumstances will this if statement's expression evaluate to `True`?

    ```python
    if __name__ == "__main__":
        pass
    ```
    <details>
    <summary>Show me</summary>

    *The expression will evaluate to `True` if the module is executed. The expression will evaluate to `False` if the module is imported (the `__name__` variable is set to the module's name in that case).*
    </details>

[<<< back](../README.md)
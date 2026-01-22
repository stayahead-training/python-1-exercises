<img src="https://github.com/stayahead-training/shared/blob/master/stayahead.png" />

# Getting Started Exercises

[<<< back](../README.md)

NB: on a Windows machine the Python executable is likely to be named `python`. On a UNIX-based machine the Python executable is likely to be named `python3`. The exercises assume a UNIX-based machine.

1. Use Python in interactive/REPL mode to compute the square of 167.

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> 167 * 167
    27889
    >>> exit()
    ```
    </details>

2. Use Python in interactive/REPL mode to compute a quarter of 75,000.

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> 75000 / 4
    18750.0
    >>> exit()
    ```
    </details>

3. Use Python in interactive/REPL mode to compute 7% of 95.

    <details>
    <summary>Show me</summary>

    ```
    $ python3
    >>> 95 * 0.07
    6.65
    >>> exit()
    ```
    </details>

4. Copy the code below into a file named **double_it.py**, save your changes, then execute the script using Python.

    ```python
    num = input("Enter a whole number: ")
    num = int(num)
    num_doubled = num * 2
    print(num, "doubled is", num_doubled)
    ```

    <details>
    <summary>Show me</summary><br />

    ```
    $ python3 double_it.py
    Enter a whole number: 5
    5 doubled is 10
    ```
</details>

5. Create a copy of the double_it.py file named **square_it.py**. Amend the script so that it squares the given number. Save your changes then execute the script using Python.

    <details>
    <summary>Show me</summary>

    File contents:

    ```python
    num = input("Enter a whole number: ")
    num = int(num)
    num_squared = num * num
    print(num, "squared is", num_squared)
    ```

    Commands:

    ```
    $ python3 square_it.py
    Enter a whole number: 5
    5 squared is 25
    ```
    </details>

6. Python code is often said to be interpreted, not compiled. What does this mean, and is it true?

    <details>
    <summary>Show me</summary>

    *Compilation is the conversion of source code (the code developers write) into machine code (the instructions the operating system understands).*
    
    *Python source code is (almost always) interpreted. That is to say the developer need not manually compile Python source code before executing it.*
    </details>

[<<< back](../README.md)
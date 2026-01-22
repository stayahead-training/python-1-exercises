<img src="https://github.com/stayahead-training/shared/blob/master/stayahead.png" />

# Strings Exercises

[<<< back](../README.md)

1. What is output by the following line of code?

    ```python
    print("What are those blue remembered hills,\nWhat spires, what farms are those?")
    ```

2. What is output by the following line of code?

    ```python
    print("He said \"feeling good is not doing good\"")
    ```

3. What is the effect of coding a string literal surrounded by triple quotes?

    <details>
    <summary>Show me</summary>

    *The string can span many lines.*
    </details>

4. What is output by the following line of code?

    ```python
    print("Hello" + "world")
    ```

5. What is output by the following line of code?

    ```python
    print("Hello", "world")
    ```

6. What is output by the following lines of code?

    ```python
    city = "birmingham"
    city.capitalize()
    print(city)
    ```

7. Copy the following code into a script named <b>data_cleanse.py</b>.

    ```python
    data = "   fred-THOMAS\n"
    ```

    Then add code to:
    - Determine the length of the first name and assign it to a variable named `first_name_length`
    - Remove whitespace from both ends of the string 
    - Replace the hyphen with a space
    - Capitalise the first letter of each name

    Finally, write the data to stdout.
    
    <details>
    <summary>Show me</summary>

    ```python
    data = "   fred-THOMAS\n"
    first_name_length = data.index("-")
    data = data.strip().replace("-", " ").title()
    print(data)
    ```
    </details>


[<<< back](../README.md)
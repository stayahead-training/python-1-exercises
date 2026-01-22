<img src="https://github.com/stayahead-training/shared/blob/master/stayahead.png" />

# Containers Exercises

[<<< back](../README.md)

1. What is output by the following lines of code?

    ```
    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> nums[1:6]
    ```

2. What is output by the following lines of code?

    ```
    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> nums[1:6:2]
    ```

3. What is output by the following lines of code?

    ```
    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> nums[2::2]
    ```

4. What is output by the following lines of code?

    ```
    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> nums[::3]
    ```

5. What is output by the following lines of code?

    ```
    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> nums[-3]
    ```

6. What is output by the following line of code?

    ```
    >>> list(range(0, 110, 10))[5::]
    ```

7. What is output by the following line of code?

    ```
    >>> "pppyyyttthhhooonnn"[::3]
    ```

8. What is output by the following lines of code?

    ```
    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> num = int(len(nums) / 2)
    >>> name = "Shakespeare"
    >>> name[nums[num - 1]]
    ```

9. Copy the following code into a script named <b>ingredients.py</b>.

    ```python
    ingredients = [
        "Beef fillet",
        "Vegetable oil",
        "Mushrooms",
        "Thyme",
        "White wine",
        "Sugar",
        "Prosciutto",
        "Puff pastry",
        "Flour"
    ]
    ```

    Then add code to:
    - Add `Egg yolks`
    - Replace `Vegetable oil` with `Olive oil`
    - Remove the `Sugar`
    - Insert `Butter` after the `Mushrooms`

    Finally, write to stdout each ingredient on a new line.
    
    <details>
    <summary>Show me</summary>

    ```python
    ingredients = [
        "Beef fillet",
        "Vegetable oil",
        "Mushrooms",
        "Thyme",
        "White wine",
        "Sugar",
        "Prosciutto",
        "Puff pastry",
        "Flour"
    ]

    ingredients.append("Egg yolks")
    ingredients[1] = "Olive oil"
    ingredients.remove("Sugar")
    ingredients.insert(3, "Butter")

    for ingredient in ingredients:
        print(ingredient)
    ```
    </details>

10. What is output by the following line of code?

    ```
    >>> (1, 2, 3)[1]
    ```

11. What is output by the following line of code?

    ```
    >>> ("Hello")
    ```

12. What is output by the following line of code?

    ```
    >>> ("Hello",)
    ```

13. Copy the following code into a script named <b>movie.py</b>.

    ```python
    movie = {
        "title": "The Blues Brothers",
        "genre": "Comedy",
        "year": 1981,
        "reviews": [],
        "actors": [
            "John Belushi",
            "Dan Ackyroyd"
        ]
    }
    ```

    Then add code to:
    - Update the year to 1980
    - Add a `cameos` key value pair that contains John Candy, Carrie Fisher, Aretha Franklin, James Brown, and Ray Charles.
    - Remove the `reviews` key value pair
    
    Finally, write to stdout each key value pair on a new line.
    
    <details>
    <summary>Show me</summary>

    ```python
    movie = {
        "title": "The Blues Brothers",
        "genre": "Comedy",
        "year": 1981,
        "reviews": [],
        "actors": [
            "John Belushi",
            "Dan Ackyroyd"
        ]
    }

    movie["year"] = 1980
    movie["cameos"] = [
        "John Candy", 
        "Carrie Fisher", 
        "Aretha Franklin", 
        "James Brown", 
        "Ray Charles"
    ]
    movie.pop("reviews")

    for key, value in movie.items():
        print(key, value)
    ```
    </details>

[<<< back](../README.md)
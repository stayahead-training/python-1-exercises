<img src="https://github.com/stayahead-training/shared/blob/master/stayahead.png" />

# Files and the Filesystem Exercises

[<<< back](../README.md)

1. Code a script that reads [this file](./pupils.txt) of pupil names into memory. For each name the script should prompt the user to enter an exam result (0-100) and then write to another file each pupil's name along with his/her exam result (comma delimited).

    <details>
    <summary>Show me</summary>

    ```python
    pupils_file = open("./pupils.txt")
    names = pupils_file.readlines()
    pupils_file.close()
    results_file = open("./results.txt", "w")
    for name in names:
        result = input(f"Enter exam result for {name}: ")
        results_file.write(f"{name},{result}\n")
    results_file.close()
    ```
    </details>

2. What's the difference between the `a` and `w` modes when opening a file?

    <details>
    <summary>Show me</summary>

    *The mode `a` enables appending to the end of the given file. The mode `w` enables writing to the file and will truncate existing content, if any. In both cases an attempt will be made to create the file if it does not exist.*
    </details>

3. Is there any difference in behaviour between the two code snippets below?

    ```python
    # snippet 1
    file = open("some_file.txt")
    lines = file.readlines()
    file.close()
    for line in lines:
        print(line)
    ```

    ```python
    # snippet 2
    file = open("some_file.txt")
    for line in file:
        print(line)
    file.close()
    ```

4. Refactor your solution to task 1 so that it includes error handling. Make sure that the file is closed regardless of whether an error is raised or not.

5. What is a context manager?

    <details>
    <summary>Show me</summary>

    *A context manager is an object whose class implements the `__enter__` and `__exit__` dunder methods.*
    
    *When instantiated in a `with` block the context manager's `__exit__` method is called at the end of the block.*

    *The object returned by the `open` function is a context manager, and its `__exit__` method closes the file.*
    </details>

6. If necessary, refactor your solution to task 1 so that it exploits the fact the object returned by the `open` function is a context manager.

7. Code a script that simulates a filesystem explorer. The user should be able to list the contents of the current directory and move between directories.

    <details>
    <summary>Show me</summary>

    ```python
    import os
    while True:
        option = input("List directory contents (list), change directory (change), or quit: ")
        if option == "list":
            for item in os.listdir():
                print(item)
        elif option == "change":
            directory = input("Directory name: ")
            os.chdir(directory)
            print(os.getcwd())
        elif option == "quit":
            print("Goodbye")
            break
        else:
            print("Invalid option")
    ```
    </details>

8. Refactor your solution to task 7 so that the script gives the user some indication as to whether each item in a directory is a file or directory. Hint: take a look at the functions in the `os.path` module.

[<<< back](../README.md)
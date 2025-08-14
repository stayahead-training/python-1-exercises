<img src="https://github.com/stayahead-training/shared/blob/master/stayahead.png" />

# Databases Exercises

[<<< back](../README.md)

1. Create a script that enables the searching (by title) of this [SQLite database](books.sqlite.db). It contains a table of `books` with `id`, `title`, `author`, and `category` columns.<details>
    <summary>Show me</summary>

    ```python
    import sqlite3

    # assuming the DB is in the same directory as the script
    conn = sqlite3.connect("books.sqlite.db")
    cursor = conn.cursor()
    sql = "select * from books where lower(title) like lower(?)"
    while True:
        user_input = input("Enter title to search or q to quit: ")
        if user_input.lower() == "q":
            print("Goodbye")
            conn.close()
            break
        partial_title = user_input
        cursor.execute(sql, [f"%{partial_title}%"])
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                Id, title, author, category = row
                print(f"{Id:<5} {title:40} {author:25} {category}")
        else:
            print("No matching books!")
    ```
</details>

2. Refactor your solution for task 1 so that some of the work is abstracted away into a function. Hint: ideally the script should give no indication that the data is stored in a database. That is, for all the script knows, the data could be stored anywhere.

3. The database includes an **empty** `reviews` table with `book_id` (foreign key), `reviewer`, and `content` columns. Refactor your solution for task 1 so that if the user's search yields results, he/she is given the option of adding a review for one of the listed books.

4. Refactor your solution for task 1 so that the user can choose to view reviews for a given book listed in the search results.

5. Refactor your solution for task 1 so that search results are cached. If the user searches for the same partial title a second time, the script should not read again from the database. Instead it should fetch the data from the cache.

[<<< back](../README.md)
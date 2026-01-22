<img src="https://github.com/stayahead-training/shared/blob/master/stayahead.png" />

# Pattern Matching Exercises

[<<< back](../README.md)

1. What is a regex?

    <details>
    <summary>Show me</summary>

    *A regex (regular expression) is a sequence of characters that forms a pattern to match against string data.*
    </details>

2. Match each of the metacharacters with its definition.

    |Metacharacter |Definition
    |--------------|----------
    |`?`           |Any character
    |`{n}`         |One or more of the previous character
    |`()`          |Zero or one of the previous character
    |`.`           |Exactly n of the previous character
    |`+`           |A group
    |`*`           |Start of the string
    |`$`           |Zero or more of the previous character
    |`^`           |End of the string

3. Which of the following strings are a match for this pattern: `^fe?t.+$` ?

    - `feet`
    - `fete`
    - `feeling`
    - `feet up`
    - `fettle`

4. Match each of the sequences with its definition.

    |Sequence      |Definition
    |--------------|----------
    |`\s`          |Not a whitespace character
    |`\W`          |A digit
    |`\b`          |The start/end of a word
    |`\d`          |A whitespace character
    |`\S`          |Not a word character

5. Which of the following strings are a match for this pattern: `^\w{2}\s\d{2}$`

    - `AB 12`
    - `12 34`
    - `a! 11`
    - `b_ 56`
    - `cds78`

6. What do the following regex sets imply?

    - `[A-z]`
    - `[£$€]`
    - `[^4-9]`

7. Create a module containing a function to verify the given string is a valid UK number plate (given current rules). Then code a script to test your module.

    <details>
    <summary>Show me</summary>

    ```python
    # my_validators.py
    def is_valid_number_plate(string):
        import re
        pattern = "^[A-Z]{2}]\d{2} [A-Z]{3}$"
        return bool(re.match(pattern, string))

    # my_validators_test.py
    import my_validators as mv
    assert mv.is_valid_number_plate("AB12 CDE")
    assert not mv.is_valid_number_plate("A12B CD3")
    ```
    </details>

8. Create a module containing a function that uses a regex to parse bank account data in the following form:

    ```python
    1234 Credit:
    David Smith,500.0
    2345 Debit:
    Sarah Jones,-150.0
    ```

    The function should return a list of dictionaries comprising the account number, customer's last name, and balance only. The input string may comprise zero or more records. Given the example data above, the function should return the following:

    ```python
    [
        {"number": 1234, "last_name": "Smith", "balance": 500.0},
        {"number": 2345, "last_name": "Jones", "balance": -150.0}
    ]
    ```

    Hint: create a pattern that exploits groups and the re module's match function. Be sure to code a script to test your module.
    
    <details>
    <summary>Show me</summary>

    ```python
    # accounts.py
    def parse_accounts(string):
        import re
        pattern = r"(\d{4}) [A-z]+:\n[A-z]+ ([A-z]+),([-\d\.]+)\n"
        results = re.findall(pattern, string)
        accounts = []
        for number, last_name, balance in results:
            accounts.append({
                "number": int(number),
                "last_name": last_name,
                "balance": float(balance)
            })
        return accounts

    # accounts_test.py
    import accounts as acc
    
    data = """
    1234 Credit:
    David Smith,500.0
    2345 Debit:
    Sarah Jones,-150.0
    """

    accounts = acc.parse_accounts(data)
    for account in accounts:
        print(account)
    ```
    </details>

[<<< back](../README.md)
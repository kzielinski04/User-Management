# User management program

## Introduction

This is a program created in Python which main purpose is managing users' data. The program provides plenty of functionality such as adding, editing, and removing users or generating strong passwords. It also validates users' data.

## Python installation

To run this program, firstly you need to install Python. Here's how to do it:

### Windows

- Download Python installer from [python.org](https://www.python.org)
- Run the installer and make sure that "Add Python to PATH" option is checked
- Click "Install Now"

### Linux (Debian/Ubuntu)

Type these instructions in terminal:
```bash
sudo apt update
sudo apt install python3
```

## Creating a virutal environment

It is recommended to use virual environments to separate your dependencies from global Python packages.
```bash
python3 -m venv venv
```

### Activating a virual environment

Windows:
```bash
venv/Scripts/activate
```

Linux:
```bash
source venv/bin/activate
```

## Requirements

- Python 3.12 or newer

## `add_user()`

`add_user()` function  adds new user to `users.json` file. It takes one argument which is a dictionary that contains user's data, such as name, pesel, nip, and regon (user id is generated automatically) The function stores that data in `users.json` file. If the file doesn't exist, it is created automatically.

## Example of usage

### Code: 
```python
user = {"user_name" : "John Smith", "user_pesel" : "02070803628", "user_nip" : "1234563218", "user_regon" : "380186266"} #Let's create a dictionary that contains the data of some user
add_user(user) #Calling add_user() function will add the data stored in user variable to users.json file
```

### Content of `users.json` after calling `add_user()` function:

```
[
    {
        "user_name": "John Smith",
        "user_pesel": "02070803628",
        "user_nip": "1234563218",
        "user_regon": "380186266",
        "user_id": 1
    }
]
```

## `load_users()`
`load_users()` function loads users from `users.json` file. If the file is empty, this function returns an empty list. Otherwise, it returns a list of dictionaries containing users' data.

## Example of usage

### Content of `users.json` file before calling `load_users()` function:

```
[
    {
        "user_name": "John Smith",
        "user_pesel": "02070803628",
        "user_nip": "1234563218",
        "user_regon": "380186266",
        "user_id": 1
    },
    {
        "user_name": "Will Jefferson",
        "user_pesel": "04211507457",
        "user_nip": "6462933516",
        "user_regon": "243510052",
        "user_id": 2
    }
]
```

### Code:

```python
users = load_users() #We call load_users function and assign its returned value to users variable
print(users) #Let's check what's inside users variable now
```

### Content of `users` variable after calling `load_users()` function

```
[{'user_name': 'John Smith', 'user_pesel': '02070803628', 'user_nip': '1234563218', 'user_regon': '380186266', 'user_id': 1}, {'user_name': 'Will Jefferson', 'user_pesel': '04211507457', 'user_nip': '6462933516', 'user_regon': '243510052', 'user_id': 2}]
```

## `remove_user()`
`remove_user()` function removes a user from `users.json` file **if the user exists in that file**.  It takes one argument which is user id (integer number) and searches the file for a user with that id. If the user is found, their data is deleted from `users.json` file. Otherwise the function ends, returning nothing.

## Example of usage

### Content of `users.json` file before calling `remove_user()` function:

```
[
    {
        "user_name": "John Smith",
        "user_pesel": "02070803628",
        "user_nip": "1234563218",
        "user_regon": "380186266",
        "user_id": 1
    },
    {
        "user_name": "Will Jefferson",
        "user_pesel": "04211507457",
        "user_nip": "6462933516",
        "user_regon": "243510052",
        "user_id": 2
    }
]
```

### Code:

```python
remove_user(1) #We want to remove a user from users.json file, whose id is equal to 1
```

### Content of `users.json` file after calling `remove_user()` function:

```
[
    {
        "user_name": "Will Jefferson",
        "user_pesel": "04211507457",
        "user_nip": "6462933516",
        "user_regon": "243510052",
        "user_id": 2
    }
]
```

## `edit_user()`

`edit_user()` function modifies the data of the user from `users.json` file **if the user exists in that file** . It takes two arguments: user id(integer number) and updated data(dictionary which contains new data for a user). The function searches the file for a user with a certain id and updates their data. If the user is not found, the function ends, returning nothing.

## Example of usage

### Content of `users.json` file before calling `edit_user()` function:

```
[
    {
        "user_name": "John Smith",
        "user_pesel": "02070803628",
        "user_nip": "1234563218",
        "user_regon": "380186266",
        "user_id": 1
    },
    {
        "user_name": "Will Jefferson",
        "user_pesel": "04211507457",
        "user_nip": "6462933516",
        "user_regon": "243510052",
        "user_id": 2
    }
]
```

### Code:
```python
updated_data = {"user_pesel" : "02283114559", "user_nip" : "8393628075", "user_regon" : "610905588" } #Let's create some new data for a user
edit_user(2, updated_data) #The function will update data of user with id equal to 2 
```

### Content of `users.json` file after calling `edit_user()` function:

```
[
    {
        "user_name": "John Smith",
        "user_pesel": "02070803628",
        "user_nip": "1234563218",
        "user_regon": "380186266",
        "user_id": 1
    },
    {
        "user_name": "Will Jefferson",
        "user_pesel": "02283114559",
        "user_nip": "8393628075",
        "user_regon": "610905588",
        "user_id": 2
    }
]
```

## `generate_password()`

`generate_password` generates a random, strong password. It always contains at least 12 characters, including special characters, numbers, and small/capital letters.

## Example of usage

### Code:

```python
my_password = generate_password() #Generating new password and assigning it to my_password variable
print(my_password) #Let's check our password
```

### Output:

```
n^1M!Azt%om&)+1
```

## `validate_pesel()`

`validate_pesel()` checks whether the user's pesel is correct. First, it checks if the length of pesel is correct (11 characters), and then it counts the value of control digit and compares it to the last digit of pesel. If everything is correct, the function returns True, otherwise it returns False.

## Example of usage

### Code:

```python
correct_pesel = "04211507457"
incorrect_pesel = "04211507458"
print(validate_pesel(correct_pesel))
print(validate_pesel(incorrect_pesel))
```

### Output:

```
True
False
```

## `validate_nip()`

`validate_nip()` checks whether the user's nip is correct. First, it checks if the length of pesel is correct (10 characters), and then it counts the value of control digit and compares it to the last digit of nip. If everything is correct, the function returns True, otherwise it returns False.

## Example of usage

### Code:
```python
correct_nip = "1234563218"
incorrect_nip = "1234563218"
print(validate_nip(correct_nip))
print(validate_nip(incorrect_nip))
```

### Output:

```
True
False
```

## `validate_nip()`

`validate_regon()` checks whether the user's regon is correct. First, it checks if the length of pesel is correct (9 or 14 characters), and then it counts the value of control digit and compares it to the last digit of nip. If everything is correct, the function returns True, otherwise it returns False.

## Example of usage

### Code:

```python
correct_regon = "380186266"
incorrect_regon = "380186265"
print(validate_regon(correct_regon))
print(validate_regon(incorrect_regon))
```

### Output:

```
True
False
```

`validate_password()`
`validate_password()` function validates the password. First it checks if the password is at least 12 characters long. Then it checks, whether it contains any common patterns (for example: qwerty, test, admin). Apart from this, the function checks if the password contains special characters, numbers, and small/capital letters. If everything is correct, the function returns True, otherwise it returns False.

## Example of usage

### Code:

```python
good_password = "n^1M!Azt%om&)+1" #Strong password
bad_password_1 = "kjAs2833LL" #Too short, lack of special characters
bad_password_2 = "kajsgu@###222qwerty" #Lack of capital letters, contains a commonly used pattern
print(validate_password(good_password))
print(validate_password(bad_password_1))
print(validate_password(bad_password_2))
```

### Output:

```
True
False
False
```

## Best practices:

### Managing users

- Make sure that the data you want to store is correct
- Check pesel/nip/regon length
- Check if pesel/nip/regon control digit is equal to the last digit of the number

### Passwords

To make sure that your password is hacker-proof, make sure to follow these few rules:
- Your password should be at least 12 characters long
- Your password should contain special characters, numbers, and small/capital letters
- Your password shouldn't contain commonly used patterns such as "admin", "qwerty", or "test"

### Storing data

- Make sure to store data in a safe place 
- Regularly back up encrypted data to prevent data loss due to accidental deletion, corruption, or malicious attacks 
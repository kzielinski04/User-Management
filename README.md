# User management program

## Introduction
This is a program created in Python. Its main purpose is managing users and their data. The program provides plenty of functionality such as adding, editing, and removing users or generating passwords. It also validates all the data.

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

## Creating virutal environment
It is recommended to use virual environments to separate your dependencies from global Python packages.
```bash
python3 -m venv venv
```

### Activating virual environment
Windows
```bash
venv/Scripts/activate
```

Linux
```bash
source venv/bin/activate
```

## Requirements
- Python 3.12 or newer

## `add_user()` function
`add_ser()` function allows to add a new user. It saves user's data such as name, pesel 
import json, os, random, re

USERS_PATH = "data/users.json"

def load_users() -> list:
    """Load users from users.json"""
    if not os.path.exists(USERS_PATH):
        return []
    with open(USERS_PATH, 'r') as file:
        users = json.load(file)
        return users
    
def add_user(user_data:dict):
    """Add new user to users.json"""
    users = load_users()
    users.append(user_data)
    with open(USERS_PATH, 'w') as file:
        json.dump(users, file)
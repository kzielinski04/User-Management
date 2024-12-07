import json, os, random, re

USERS_PATH = "data/users.json"

def load_users() -> list:
    """Load users from users.json"""
    if not os.path.exists(USERS_PATH):
        return []
    with open(USERS_PATH, 'r') as file:
        users = json.load(USERS_PATH)
        return users
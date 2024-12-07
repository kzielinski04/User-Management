import json, os, random, re

USERS_PATH = "data/users.json"

def validate_pesel(user_pesel:str) -> bool:
    pass

def validate_nip(user_nip:str) -> bool:
    pass

def validate_regon(user_regon:str) -> bool:
    pass

def load_users() -> list:
    """Load users from users.json"""
    if not os.path.exists(USERS_PATH):
        return []
    with open(USERS_PATH, 'r') as file:
        users = json.load(file)
        return users
    
def add_user(user_data:dict):
    """Add new user to users.json"""
    if validate_pesel(user_data["user_pesel"]) == False or validate_nip(user_data["user_nip"]) == False or validate_regon(user_data["user_regon"]) == False:
        return
    users = load_users()
    users.append(user_data)
    with open(USERS_PATH, 'w') as file:
        json.dump(users, file, indent = 4)

def remove_user(user_id:int):
    """Remove user from users.json"""
    users = load_users()
    updated_users = [users for user in users if users["user_id"] != user_id]
    if len(users) != len(updated_users):
        with open(USERS_PATH, 'r') as file:
            json.dump(updated_users, file, indent = 4)

def edit_user(user_id:int, updated_data:dict):
    """Edit user from user.json"""
    if validate_pesel(updated_data["user_pesel"]) == False or validate_nip(updated_data["user_nip"]) == False or validate_regon(updated_data["user_regon"]) == False:
        return
    users = load_users()
    for user in users:
        if user["user_id"] == user_id:
            user.update(updated_data)
    with open(USERS_PATH, 'w') as file:
        json.dump(users, file, indent = 4)
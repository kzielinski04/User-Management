import json, random, re, os
USERS_FILE = "data/users.json"
user_data = {"id" : 0, "name" : "name", "nip" : "", "pesel" : "", "regon" : ""}
updated_data = {"id" : 12, "name" : "nasdasd", "nip" : "111", "pesel" : "1112", "regon" : "123"}

def validate_nip(nip:str) -> bool:
    """Validate user's NIP"""
    pass

def validate_pesel(pesel:str) -> bool:
    """Validate user's PESEL"""
    pass

def validate_regon(regon:str) -> bool:
    """Validate user's REGON"""
    pass

def load_users():
    """Load users' data from users.json"""
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def add_user(user_data:dict):
    """Add new user to users.json"""
    users = load_users()
    users.append(user_data)
    validate_nip(user_data["nip"])
    validate_pesel(user_data["pesel"])
    validate_regon(user_data["regon"])
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent = 5)

def edit_user(user_id, updated_data:dict):
    """Edit user's data from users.json"""
    users = load_users()
    with open(USERS_FILE, 'w') as f:
        for user in users:
            if user["id"] == user_id:   
                user = updated_data
            else:
                print("User not found!\n")

edit_user(0, updated_data)
import json, os, random, re

USERS_PATH = "data/users.json"

def validate_pesel(user_pesel:str) -> bool:
    """Validate user's pesel"""
    if len(user_pesel) != 11:
        return False
    control_digit = int(user_pesel[10])
    sum = 0
    for i in range(len(user_pesel)):
        current_digit = int(user_pesel[i])
        if i == 0:
            if current_digit * 1 > 9:
                temp = str(current_digit)
                temp = temp[-1]
                sum += int(temp)
            else:
                sum += current_digit * 1
        if i == 1:
            if current_digit * 3 > 9:
                temp = str(current_digit * 3)
                temp = temp[-1]
                sum += int(temp)
            else:
                sum += current_digit * 3
        if i == 2:
            if current_digit * 7 > 9:
                temp = str(current_digit * 7)
                temp = temp[-1]
                sum += int(temp)
            else:
                sum += current_digit * 7
        if i == 3:
            if current_digit * 9 > 9:
                temp = str(current_digit * 9)
                temp = temp[-1]
                sum += int(temp)
            else:
                sum += current_digit * 9
        if i == 4:
            if current_digit * 1 > 9:
                temp = str(current_digit)
                temp = temp[-1]
                sum += int(temp)
            else:
                sum += current_digit * 1
        if i == 5:
            if current_digit * 3 > 9:
                temp = str(current_digit * 3)
                temp = temp[-1]
                sum += int(temp)
            else:
                sum += current_digit * 3
        if i == 6:
            if current_digit * 7 > 9:
                temp = str(current_digit * 7)
                temp = temp[-1]
                sum += int(temp)
            else:
                sum += current_digit * 7
        if i == 7:
            if current_digit * 9 > 9 :
                temp = str(current_digit * 9)
                temp = temp[-1]
                sum += int(temp)
            else:
                sum += current_digit * 9
        if i == 8:
            if current_digit * 1 > 9:
                temp = str(current_digit)
                temp = temp[-1]
                sum += int(temp)
            else:
                sum += current_digit * 1    
        if i == 9:
            if current_digit * 3 > 9:
                temp = str(current_digit * 3)
                temp = temp[-1]
                sum += int(temp)
            else:
                sum += current_digit * 3
    if sum > 9:
        temp = str(sum)
        temp = temp[-1]
        sum = int(temp)
    sum = 10 - sum
    if sum == control_digit:
        return True
    else:
        return False

def validate_nip(user_nip:str) -> bool:
    """Validate user's nip"""
    if len(user_nip) != 10:
        return False
    last_digit = int(user_nip[9])
    sum = 0
    for i in range(len(user_nip)):
        current_digit = int(user_nip[i])
        if i == 0:
            sum += current_digit * 6
        if i == 1:
            sum += current_digit * 5
        if i == 2:
            sum += current_digit * 7
        if i == 3:
            sum += current_digit * 2
        if i == 4:
            sum += current_digit * 3
        if i == 5:
            sum += current_digit * 4
        if i == 6:
            sum += current_digit * 5
        if i == 7:
            sum += current_digit * 6
        if i == 8:
            sum += current_digit * 7
    sum %= 11
    if sum == last_digit:
        return True
    else:
        return False

def validate_regon(user_regon:str) -> bool:
    """Validate user's regon"""
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
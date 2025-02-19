import re
import sqlite3
from PIL import Image

def email_validator(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
    compiled_pattern = re.compile(pattern)
    match = compiled_pattern.fullmatch(email)
    return bool(match)

def password_check(passwd):
    special_symbols = ['$', '@', '#', '%']
    if len(passwd) < 6:
        print('Długość hasła powinna wynosić co najmniej 6 znaków')
        return False
    if len(passwd) > 20:
        print('Długość hasła nie powinna przekraczać 20 znaków')
        return False
    if not any(char.isdigit() for char in passwd):
        print('Hasło powinno zawierać co najmniej jedną cyfrę')
        return False
    if not any(char.isupper() for char in passwd):
        print('Hasło powinno zawierać co najmniej jedną wielką literę')
        return False
    if not any(char.islower() for char in passwd):
        print('Hasło powinno zawierać co najmniej jedną małą literę')
        return False
    if not any(char in special_symbols for char in passwd):
        print('Hasło powinno zawierać co najmniej jeden z symboli $@#%')
        return False
    return True

def convert_to_binary_data(file_path):
    with open(file_path, 'rb') as file:
        blob_data = file.read()
    return sqlite3.Binary(blob_data)

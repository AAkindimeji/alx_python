#!/usr/bin/python3

def validate_password(password):
    if (
        len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        ' ' not in password
    ):
        return True
    else:
        return False
validate_password = __import__('6-password').validate_password
print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))
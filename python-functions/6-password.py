def validate_password(password):

    if len(password) < 8:
        return False

  
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

   
    if ' ' in password:
        return False

    
    return has_uppercase and has_lowercase and has_digit

print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))

def isPasswordStrong(password):
    """
        Check if the password meets the strength criteria.
    """
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    if not any(char.isupper() for char in password):
        return "Weak: Password must include at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Weak: Password must include at least one lowercase letter."
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password must include at least one digit."
    
    if not any(char in '!@#$%^&*(),.?":{}|<>' for char in password):
        return "Weak: Password must include at least one special character."
    
    return "Strong: Password meets all the criteria."

def validateInput(password):
    """
        Validate the input to ensure it's not empty.
    """
    if not password:
        return False
    return True

def main():
    while True:
        password = input("Enter your password: ").strip()
        if not validateInput(password):
            print("Invalid input! Password cannot be empty.")
        else:
            break

    result = isPasswordStrong(password)
    print(f"\nPassword Strength: {result}")

main()
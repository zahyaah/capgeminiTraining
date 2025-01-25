def isPalindrome(value):
    """
        Check if the given string or number is a palindrome.
    """
    valueStr = str(value)
    return valueStr == valueStr[::-1]


def validateInput(value):
    """
        Validate the input to ensure it is not empty or invalid.
    """
    if not value:
        return False
    return True

def main():
    while True:
        userInput = input("\nEnter a string or number to check (or type 'exit' to quit): ").strip()
        
        if userInput.lower() == 'exit':
            print("bye!")
            break
        
        if not validateInput(userInput):
            print("Invalid input! Please enter a valid string or number.")
            continue

        if isPalindrome(userInput):
            print(f"'{userInput}' is a palindrome!")
        else:
            print(f"'{userInput}' is not a palindrome.")



main()
def isValidLeapYear(year):
    """
        Check if a year is a leap year.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def validateInput(yearInput):
    """
        Validate the input to ensure it is a non-negative integer.
    """
    if yearInput.isdigit():
        return True
    return False

def main():
    while True:
        userInput = input("\nEnter a year (or type 'exit' to quit): ").strip()
        
        if userInput.lower() == 'exit':
            print("bye!")
            break
        
        if not validateInput(userInput):
            print("Invalid input! Please enter a non-negative integer.")
            continue
        
        
        year = int(userInput)
        if isValidLeapYear(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")



main()
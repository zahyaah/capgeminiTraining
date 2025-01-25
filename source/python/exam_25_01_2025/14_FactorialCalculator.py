def calculateFactorial(number):
    """
        Calculate the factorial of a number using a loop
    """
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

def validateInput(value):
    """
        Validate the input to ensure it is a nonn egative integer
    """
    if not value.isdigit():
        return False, "Input must be a non negative integer."
    return True, ""

def main():
    while True:
        userInput = input("\nEnter a non negative integer to calculate its factorial (or type 'exit' to quit): ").strip()
        
        if userInput.lower() == 'exit':
            print("bye!!")
            break

        isValid, errorMessage = validateInput(userInput)
        if not isValid:
            print(f"Invalid input! {errorMessage}")
            continue

        number = int(userInput)
        

        factorial = calculateFactorial(number)
        print(f"The factorial of {number} is {factorial}.")


main()
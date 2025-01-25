def isValidNumber():
    """Validate user input to ensure it is a positive integer."""

    while True:
        userInput = input("Enter a number: ").strip()
        if userInput.isdigit() and int(userInput) > 0:
            return int(userInput)
        else:
            print("Invalid input! Please enter a positive integer.")



def fizzBuzz(number):
    """Print Fizz, Buzz, or FizzBuzz based on the number's divisibility."""

    for num in range(1, number + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def main():
    number = isValidNumber()
    print(f"\nPrinting FizzBuzz for numbers 1 to {number}:")
    fizzBuzz(number)



main()
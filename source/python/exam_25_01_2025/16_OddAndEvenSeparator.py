def getValidatedNumbers():
    """
        Prompt the user to enter a list of numbers and validate the input.
    """
    while True:
        userInput = input("Enter a list of numbers separated by spaces: ").strip()
        try:
            numbers = [int(num) for num in userInput.split()]
            return numbers
        except ValueError:
            print("Invalid input! Please enter only integers separated by spaces.")

def separateOddEven(numbers):
    """
        Separate the given list of numbers into odd and even lists.
    """
    oddNumbers = [num for num in numbers if num % 2 != 0]
    evenNumbers = [num for num in numbers if num % 2 == 0]
    
    return oddNumbers, evenNumbers

def displayResults(oddNumbers, evenNumbers):
    """
        Display the separated odd and even lists.
    """
    print("\nOdd Numbers:", oddNumbers if oddNumbers else "None")
    print("Even Numbers:", evenNumbers if evenNumbers else "None")

def main():
    numbers = getValidatedNumbers()
    oddNumbers, evenNumbers = separateOddEven(numbers)
    displayResults(oddNumbers, evenNumbers)



main()
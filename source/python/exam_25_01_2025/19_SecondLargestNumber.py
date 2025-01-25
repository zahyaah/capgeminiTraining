def getValidatedList():
    """Get and validate the list of numbers from the user."""

    while True:
        userInput = input("Enter numbers separated by spaces: ").strip()
        try:
            numList = [int(num) for num in userInput.split()]
            if len(numList) < 2:
                print("Please enter at least two numbers.")
                continue
            return numList
        except ValueError:
            print("Invalid input! Please enter a list of integers.")

def findSecondLargest(numbers):
    """Find and return the second largest number in the list."""

    uniqueNumbers = list(set(numbers))
    uniqueNumbers.sort()
    if len(uniqueNumbers) < 2:
        return None
    return uniqueNumbers[-2]

def main():
    while True:
        numbers = getValidatedList()
        secondLargest = findSecondLargest(numbers)

        if secondLargest is not None:
            print(f"The second largest number is: {secondLargest}")
        else:
            print("There is no second largest number (all numbers are the same or there's only one number).")

        continueSearch = input("\nDo you want to find another second largest number? (yes/no): ").strip().lower()
        
        if continueSearch != "yes":
            print("bye!!!")
            break


main()
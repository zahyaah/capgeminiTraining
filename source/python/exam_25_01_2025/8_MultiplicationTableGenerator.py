def getNumber():
    """
        Get a valid number from the user.
    """
    while True:
        try:
            number = int(input("Enter the number for the multiplication table: "))
            return number
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def getRange():
    """
        Get a valid range for the multiplication table from the user.
    """
    while True:
        try:
            start = int(input("Enter the starting value of the range: "))
            end = int(input("Enter the ending value of the range: "))
            if start > end:
                print("Starting value must be less than or equal to the ending value.")
            else:
                return start, end
        except ValueError:
            print("Invalid input! Please enter valid integers.")

def generateMultiplicationTable(number, start, end):
    """
        Generate and print the multiplication table for the given number and range.
    """
    print(f"\nMultiplication table for {number} from {start} to {end}:\n")
    for i in range(start, end + 1):
        print(f"{number} x {i} = {number * i}")


def main():
    number = getNumber()
    start, end = getRange()
    generateMultiplicationTable(number, start, end)


main()
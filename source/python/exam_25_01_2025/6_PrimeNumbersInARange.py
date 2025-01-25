import math

def getInput():
    """
        Get user input for the lower and upper bounds
    """
    while True:
        try:
            lowerBound = int(input("Enter first number: "))
            upperBound = int(input("Enter second number: "))
            if lowerBound >= upperBound:
                print("Lower bound must be less than the upper bound. Try again.")
                continue
            return (lowerBound, upperBound)
        except ValueError:
            print("Invalid input! Please enter valid integers.")

def primeNumber(n):
    """
        Check if a number is prime.
    """
    if n < 2:
        return False
    if n <= 3:
        return True 
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    
    return True

def main():
    lowerBound, upperBound = getInput()

    for i in range(lowerBound, upperBound):
        if primeNumber(i):
            print(i)

main()
def getInput():
    numberOne = int(input("Enter first number: "))
    numberTwo = int(input("Enter second number: "))
    numberThree = int(input("Enter third number: ")) 

    return (numberOne, numberTwo, numberThree)

def largest(a, b, c):
    if (a > b and a > c):
        return (a, 1)
    elif (b > a and b > c):
        return (b, 2)
    elif (c > a and c > b):
        return (c, 3)
    return (-1, -1)

def printLargest(largest, present):
    print(f"The largest number is {largest}")

def main():
    a, b, c = getInput()
    storeLargestNumber, index = largest(a, b, c)
    d = int(input("Enter fourth number: "))
    if (d > storeLargestNumber):
        print(f'Largest number is {d} which is the 4 number')
    else:
        print(f'Largest number is {storeLargestNumber} which is the {index} number')
    

main()
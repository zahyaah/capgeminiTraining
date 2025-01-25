def getRows():
    '''
        Takes input from the user: number of rows
    '''
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            if (rows < 0):
                print("Please enter a positive integer.")
                continue
            return rows
        except ValueError:
            print("Please enter a valid number.")

def isReverse():
    '''
        Takes a boolean input to check if the pattern needs to be inverted or not. 
    '''
    while True: 
        try:
            isReverse = input("In reverse order? (y/n): ").lower().strip()
            
            if isReverse == "y":
                return True
            elif isReverse == "n":
                return False
            else:
                print("Please enter a valid input!")
                continue 
        except ValueError:
            print("Please enter a valid input")

def pattern(rows, isInverted):
    '''
        Method used to generate pattern
    '''
    if (isInverted):
        for i in range(rows, 0, -1):
            print('*'*i)
    else:
        for i in range(rows):
            print('*'*i)


def main():
    numberOfRows = getRows()
    isInverted = isReverse()
    pattern(numberOfRows, isInverted) 


main()
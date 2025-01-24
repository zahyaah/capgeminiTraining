def get_input():
    '''
        takes user input
    '''
    a = int(input("Enter first number: ")) 
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    d = int(input("Enter fourth number: "))
    e = int(input("Enter the divisor for the four numbers: "))
    return (a, b, c, d, e)


def getSum(a, b, c, d):
    '''
        sums all the 4 numbers
    '''

    sum = a+b+c+d  
    return sum 

def average(sum, e):
    '''
        calculates the average of 4 numbers by e. 
    '''
    avg = sum/e
    return avg 

def printAverage(data):
    '''
    simply prints the average of 4 numbers numbers (returned by average() function)
    '''
    print(f"The average is {data}")


def main():
    a, b, c, d, e= get_input()
    sum = getSum(a, b, c, d)
    avg = average(sum, e)
    printAverage(avg)

main()

    


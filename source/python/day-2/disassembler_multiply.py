import dis

def getInput():
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))
    return firstNumber, secondNumber 


def multiply(firstNumber, secondNumber):
    return firstNumber*secondNumber

def printOutput(product):
    print(f"The product is {product}")

def multiplySecond():
    product = 1
    for i in range(5):
        product = product * i
    return product 

def main(): 
    # firstNumber, secondNumber = getInput()
    # product = multiply(firstNumber, secondNumber)
    # printOutput(product)
    # dis.dis(getInput)
    # dis.dis(multiply)
    # dis.dis(printOutput)
    dis.dis(multiplySecond)
   

main()

def amountPerPerson(totalBill, numPeople, tipPercentage):
    """
        Calculate the amount each person has to pay.
    """
    total_amount = totalBill + (totalBill * tipPercentage / 100)
    return total_amount / numPeople

def validateInput(value, value_type):
    """
        Validate user input for non-negative numbers.
    """
    try:
        value = value_type(value)
        if value < 0:
            return False
        return True
    except ValueError:
        return False

def main():
    while True:
        totalBill = input("Enter the total bill amount: ").strip()
        if not validateInput(totalBill, float):
            print("Invalid input! Please enter a positive number.")
        else:
            totalBill = float(totalBill)
            break


    while True:
        numPeople = input("Enter the number of people: ").strip()
        if not validateInput(numPeople, int) or int(numPeople) == 0:
            print("Invalid input! Please enter a positive integer greater than 0.")
        else:
            numPeople = int(numPeople)
            break


    while True:
        tipPercentage = input("Enter the tip percentage (if any): ").strip()
        if not validateInput(tipPercentage, float):
            print("Invalid input! Please enter a positive number.")
        else:
            tipPercentage = float(tipPercentage)
            break

    perPerson = amountPerPerson(totalBill, numPeople, tipPercentage)
    print(f"\nEach person has to pay: {perPerson} rupees")


main()
balance = 0

def check_balance():
    '''
        Display the current account balance.
    '''
    print(f"\nYour current balance is {balance}\n")

def depositMoney(moneyToBeDeposited):
    '''
        Deposit a specified amount into the account
    '''
    global balance
    if (isinstance(moneyToBeDeposited, float) or isinstance(moneyToBeDeposited, int)):
        balance += moneyToBeDeposited
        print(f"\nAmount deposited: {moneyToBeDeposited}.\n")
    else:
        print("INVALID TYPE.")

def withdrawMoney(moneyToBeWithdrawn):
    '''
        Withdraw a specified amount from the account if funds are sufficient
    '''
    global balance
    if (isinstance(moneyToBeWithdrawn, float) or isinstance(moneyToBeWithdrawn, int)):
        if (moneyToBeWithdrawn < balance):
            balance -= moneyToBeWithdrawn
            print(f"\nAmount withdrawn: {moneyToBeWithdrawn}\n")
        else:
            print("\nInsufficient funds.\n")

        
def main():
    while True:
        print("1. Check balance.")
        print("2. Deposit Money.")
        print("3. Withdraw Money.")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if (choice.isdigit()):
            choice = int(choice)
            if (choice == 1):
                check_balance()
            elif (choice == 2):
                moneyToBeDeposited = int(input("Enter the amount to be deposited: "))
                depositMoney(moneyToBeDeposited)
            elif (choice == 3):
                moneyToBeWithdrawn = int(input("Enter the money to be withdrawn: "))
                withdrawMoney(moneyToBeWithdrawn)
            elif (choice == 4):
                print("Bye.")
                break; 
            else:
                print("Invalid Choice.")
        else:
            print("Invalid choice.")
            continue

main()

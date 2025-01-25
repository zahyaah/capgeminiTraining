def isEligible(salary, age, creditScore):
    """
        Check loan eligibility based on salary, age, and credit score
    """
    if salary < 30000:
        return "Rejected: Salary is too low."
    elif age < 21 or age > 60:
        return "Rejected: Age is not within the eligible range."
    elif creditScore < 650:
        return "Rejected: Credit score is too low."
    else:
        return "Approved: Loan eligibility confirmed."


def validate(value, valueType):
    """
        Validate user input for positive numbers
    """
    try:
        value = valueType(value)
        if value < 0:
            return False
        return True
    except ValueError:
        return False


def main():
    while True:
        salary = input("Enter your salary: ").strip()
        if not validate(salary, float):
            print("Invalid input! Please enter a positive number.")
        else:
            salary = float(salary)
            break


    while True:
        age = input("Enter your age: ").strip()
        if not validate(age, int) or int(age) < 0:
            print("Invalid input! Please enter a positive integer.")
        else:
            age = int(age)
            break

    while True:
        creditScore = input("Enter your credit score: ").strip()
        if not validate(creditScore, int) or int(creditScore) < 0:
            print("Invalid input! Please enter a positive integer.")
        else:
            creditScore = int(creditScore)
            break



    result = isEligible(salary, age, creditScore)
    print(f"\nLoan Status: {result}")



main()
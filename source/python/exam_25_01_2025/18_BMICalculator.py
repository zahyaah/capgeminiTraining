def calculateBmi(weight, height):
    """
        Calculate BMI using weight and height
    """

    return weight / (height ** 2)

def getBmiCategory(bmi):
    """
        Determine the BMI category based on BMI value
    """

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def getValidatedInput(prompt):
    """
        Get and validate numerical input from the user
    """
    
    while True:
        userInput = input(prompt).strip()
        try:
            return float(userInput)
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    weight = getValidatedInput("Enter your weight (in kg): ")
    height = getValidatedInput("Enter your height (in meters): ")

    bmi = calculateBmi(weight, height)
    
    category = getBmiCategory(bmi)
    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")



main()
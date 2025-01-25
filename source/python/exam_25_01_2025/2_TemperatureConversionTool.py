def celsiusToFahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def celsiusToKelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def fahrenheitToCelsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def fahrenheitToKelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return fahrenheitToCelsius(fahrenheit) + 273.15

def kelvinToCelsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def kelvinToFahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return celsiusToFahrenheit(kelvinToCelsius(kelvin))

def getValidatedInput(prompt):
    """Get and validate numerical input from the user."""
    while True:
        userInput = input(prompt).strip()
        try:
            return float(userInput)
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    while True:
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin")
        print("5. Kelvin to Celsius")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        
        if choice not in {"1", "2", "3", "4", "5", "6", "7"}:
            print("Invalid choice! Please select a valid option.")
            continue

        if choice == "7":
            print("Goodbye!")
            break

        temperature = getValidatedInput("Enter the temperature: ")
        if choice == "1":
            print(f"\n\nResult: {celsiusToFahrenheit(temperature)} F")
        elif choice == "2":
            print(f"\n\nResult: {celsiusToKelvin(temperature)} K")
        elif choice == "3":
            print(f"\n\nResult: {fahrenheitToCelsius(temperature)} C")
        elif choice == "4":
            print(f"\n\nResult: {fahrenheitToKelvin(temperature)} K")
        elif choice == "5":
            print(f"\n\nResult: {kelvinToCelsius(temperature)} C")
        elif choice == "6":
            print(f"\n\nResult: {kelvinToFahrenheit(temperature)} F")



main()
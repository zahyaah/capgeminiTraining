print("hello world")
name = input().split(" ")

print(f'Hello {name[0]} {name[1]}')

firstName = input("Enter your first name: ").title()
lastName = input("Enter your last name: ").title()
print(f'hello, i am {lastName}, {firstName} {lastName}') 

pincode = int(input("Enter your pincode: ")) 
location = input("Enter your current location: ").title()
print(f'{firstName} {lastName} lives in {location} - ({pincode})')
firstNumber = int(input("Enter first number: "))

secondNumber = int(input("Enter second number: "))
print(firstNumber+secondNumber)

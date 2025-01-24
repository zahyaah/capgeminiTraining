import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

discriminant = (b**2) - (4*a*c)
first_root = (-b+math.sqrt(discriminant))/(2*a)
second_root = (-b-math.sqrt(discriminant))/(2*a)

print(first_root)
print(second_root)
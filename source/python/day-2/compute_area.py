def display(data):
    print(f"The area is {data}")

def get_input():
    received_length = int(input("Enter length: "))
    received_breadth = int(input("Enter breadth: "))

    return (received_length, received_breadth)

def compute_area(length, breadth):
    return (length*breadth)

def main():
    L, B = get_input()
    area = compute_area(L, B)
    display(area)

main()

    
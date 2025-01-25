def addItemToCart(cart):
    """
        Adds an item (name and price) to the cart
    """

    while True:
        itemName = input("Enter the item name: ").strip()

        if not itemName:
            print("Item name cannot be empty. Try again.")
            continue
        
        try:
            itemPrice = float(input("Enter the item price: ").strip())
            if itemPrice < 0:
                print("Price cannot be negative. Try again.")
                continue


            cart.append((itemName, itemPrice))
            print(f"{itemName} added to the cart.")
            break
        except ValueError:
            print("Invalid price! Please enter a valid number.")


def viewCart(cart):
    """
        Displays all items in the cart and the total price.
    """


    if not cart:
        print("Your cart is empty.")
    else:
        totalPrice = 0
        print("\nItems in your cart:")
        for item in cart:
            print(f"{item[0]} - : {item[1]} rupees")
            totalPrice += item[1]
        print(f"Total Price - : {totalPrice:.2f} rupees\n")

def main():
    """
        Main function to manage the shopping cart actions
    """
    cart = []

    while True:
        print("\n1. Add item to cart")
        print("2. View cart")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice (1/2/3): ").strip())
            if choice == 1:
                addItemToCart(cart)
            elif choice == 2:
                viewCart(cart)
            elif choice == 3:
                print("Thank you for shopping with us! Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 3.")


main()
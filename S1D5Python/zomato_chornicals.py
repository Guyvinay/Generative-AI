
def display_menu(menu):
    print("Menu:")
    for dish_id, dish_info in menu.items():
        print(f"{dish_id}. {dish_info['name']} - ${dish_info['price']:.2f} ({'Available' if dish_info['availability'] else 'Not Available'})")

def add_new_dish(menu):
    new_dish_id = len(menu) + 1
    new_dish_name = input("Enter the name of the new dish: ")
    new_dish_price = float(input("Enter the price of the new dish: "))
    new_dish_availability = input("Is the new dish available? (yes/no): ").lower() == "yes"

    new_dish = {
        "name": new_dish_name,
        "price": new_dish_price,
        "availability": new_dish_availability
    }

    menu[new_dish_id] = new_dish

    print(f"{new_dish_name} has been added to the menu with ID {new_dish_id}.")

def main():
    print("Welcome to Zomato Chronicles: The Great Food Fiasco!")

    menu = {
        1: {
            "name": "Pizza",
            "price": 12.99,
            "availability": True
        },
        2: {
            "name": "Burger",
            "price": 8.99,
            "availability": False
        },
        # Add more dishes to the menu.
    }

    while True:
        print("\nOptions:")
        print("1. Display Menu")
        print("2. Add a New Dish")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            display_menu(menu)
        elif choice == "2":
            add_new_dish(menu)
        elif choice == "3":
            print("Exiting Zomato Chronicles. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


# def main():
#     print("Welcome to Zomato Chroniclas: The Great Grand Food Finch! ")

# menu = {
#     1: {
#         "name": "Pizza",
#         "price": 12.99,
#         "availability": True
#     },
#     2: {
#         "name": "Burger",
#         "price": 8.99,
#         "availability": False
#     },
#     3: {
#         "name": "Dhosa",
#         "price": 12.99,
#         "availability": True
#     },
#     4: {
#         "name": "Fries",
#         "price": 8.99,
#         "availability": False
#     },

#     # Add more dishes to the menu.
# }

# print("Menu: ")
# for dish_id, dish_info in menu.items():
#         print(f"{dish_id}. {dish_info['name']} -  &{dish_info['price']:.2f} ( {'Available' if dish_info['availability'] else 'Not Available' }) ")

# new_dish_id = len(menu) + 1  # Generate a unique dish ID
# new_dish_name = input("Enter the name of the new dish: ")
# new_dish_price = float(input("Enter the price of the new dish: "))
# new_dish_availability = input("Is the new dish available? (yes/no): ").lower() == "yes"

#  # Create a dictionary for the new dish
# new_dish = {
#         "name": new_dish_name,
#         "price": new_dish_price,
#         "availability": new_dish_availability
#     }

# menu[new_dish_id]=new_dish

#   # Print a confirmation message
# print(f"{new_dish_name} has been added to the menu with ID {new_dish_id}.")



# if __name__ == "__main__":
#     main()
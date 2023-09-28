
import os
import pickle

# Initialize menu and orders as empty dictionaries
menu = {}
orders = {}

# Function to display the menu
def display_menu():
    print("\n** Menu **")
    for dish_id, details in menu.items():
        print(f"{dish_id}: {details['name']} - ${details['price']} ({'Available' if details['available'] else 'Not Available'})")

# Function to add a new dish to the menu
def add_dish():
    dish_id = input("Enter Dish ID: ")
    name = input("Enter Dish Name: ")
    price = float(input("Enter Dish Price: "))
    available = input("Is it available? (yes/no): ").lower() == 'yes'

    menu[dish_id] = {'name': name, 'price': price, 'available': available}
    print(f"{name} has been added to the menu!")

# Function to remove a dish from the menu
def remove_dish():
    dish_id = input("Enter Dish ID to remove: ")
    if dish_id in menu:
        del menu[dish_id]
        print("Dish removed from the menu.")
    else:
        print("Dish not found in the menu.")

# Function to update dish availability
def update_availability():
    dish_id = input("Enter Dish ID to update availability: ")
    if dish_id in menu:
        available = input("Is it available now? (yes/no): ").lower() == 'yes'
        menu[dish_id]['available'] = available
        print(f"Availability for {menu[dish_id]['name']} updated.")
    else:
        print("Dish not found in the menu.")

# Function to take a new order
def take_order():
    customer_name = input("Enter Customer Name: ")
    order_items = input("Enter Dish IDs (comma-separated): ").split(',')
    order_id = len(orders) + 1

    order = {
        'customer_name': customer_name,
        'order_items': order_items,
        'status': 'received',
        'total_price': sum(menu[item]['price'] for item in order_items if item in menu)
    }

    orders[order_id] = order
    print(f"Order received! Order ID: {order_id}")

# Function to update order status
def update_order_status():
    order_id = int(input("Enter Order ID to update status: "))
    if order_id in orders:
        new_status = input("Enter new status (preparing/ready for pickup/delivered): ")
        orders[order_id]['status'] = new_status
        print(f"Order {order_id} status updated to {new_status}.")
    else:
        print("Order not found.")

# Function to review all orders
def review_orders():
    print("\n** Orders **")
    for order_id, order in orders.items():
        print(f"Order ID: {order_id}")
        print(f"Customer Name: {order['customer_name']}")
        print(f"Status: {order['status']}")
        print("Ordered Items:")
        for item in order['order_items']:
            if item in menu:
                print(f"{menu[item]['name']} - ${menu[item]['price']}")
        print(f"Total Price: ${order['total_price']}\n")

# Function to save menu and orders data to a file
def save_data():
    with open("zesty_zomato_data.pkl", "wb") as file:
        pickle.dump({'menu': menu, 'orders': orders}, file)

# Function to load menu and orders data from a file
def load_data():
    global menu, orders
    if os.path.exists("zesty_zomato_data.pkl"):
        with open("zesty_zomato_data.pkl", "rb") as file:
            data = pickle.load(file)
            menu = data['menu']
            orders = data['orders']

# Main loop for user interaction
load_data()
while True:
    print("\n** Zesty Zomato Management System **")
    print("1. Display Menu")
    print("2. Add Dish")
    print("3. Remove Dish")
    print("4. Update Dish Availability")
    print("5. Take Order")
    print("6. Update Order Status")
    print("7. Review Orders")
    print("8. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        display_menu()
    elif choice == '2':
        add_dish()
    elif choice == '3':
        remove_dish()
    elif choice == '4':
        update_availability()
    elif choice == '5':
        take_order()
    elif choice == '6':
        update_order_status()
    elif choice == '7':
        review_orders()
    elif choice == '8':
        save_data()
        print("Exiting Zesty Zomato Management System. Have a great day!")
        break
    else:
        print("Invalid choice. Please try again.")

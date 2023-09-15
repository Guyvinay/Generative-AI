'''snackInventory={}
salesRecords={}

def addSnak():
    snackId=input("Enter id of snak:- ")
    snakName=input("Enter name of snak:- ")
    snakPrice=input("Enter price of snak:- ")
    snackAvail=input("Snack Availability?(yes/no:- )").lower()

    snackInventory[snackId]={
        "snackName":snakName,
        "snackPrice":snakPrice,
        "snackAvail":snackAvail
    }
    print(f"Snack {snakName} successfully added to inventory ")

def removeSnak():
    snackId=input("Enter id of snack you want to remove:- ")
    if snackId in snackInventory :
        del snackInventory[snackId]
        print(f"Snack with id {snackId} removed from inventory ")
    else :
       print(f"Snack with id {snackId} is not available in inventory ")    

def updateAvailability():
    snackId=input("Enter id of snack you want to update availability:- ")
    if snackId in snackInventory :
        avail=input("Is snack available? (yes/no):- ").lower()
        snackInventory[snackId]["snackAvail"]=avail == "yes"
        print(f"Availability of snack '{snackInventory[snackId]['snackName']}' updated.")
    else: 
        print(f"Snack with ID '{snackId}' not found in the inventory.")


def recordSale():
    snackId=input("Enter id of Snack:- ")
    if snackId in snackInventory :
        if snackInventory[snackId]["snackAvail"]:
            snackQuant=input("ENter Number of Snack:- ")
            if snackId in salesRecords :
                salesRecords[snackId]+=snackQuant
            else :
                salesRecords[snackId]=snackQuant  
                print(f"Sale recorded for snack '{snackInventory[snackId]['snackName']}'.")
            snackInventory[snackId]["snackAvail"] = False
        else:
            print(f"Snack '{snackInventory[snackId]['name']}' is not available.")
    else:
        print(f"Snack with ID '{snackId}' not found in the inventory.")
    

while True:
    print("\nMumbai Munchies Inventory Management System")
    print("1. Add a snack to the inventory")
    print("2. Remove a snack from the inventory")
    print("3. Update snack availability")
    print("4. Record a sale")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        addSnak()
    elif choice == "2":
        removeSnak()
    elif choice == "3":
        updateAvailability()
    elif choice == "4":
        recordSale()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please choose a valid option.")'''

        # Initialize the snack inventory as a dictionary
snack_inventory = {}

# Initialize the sales record as a dictionary
sales_record = {}

# Function to add a snack to the inventory
def add_snack():
    snack_id = input("Enter snack ID: ")
    snack_name = input("Enter snack name: ")
    price = float(input("Enter snack price: "))
    available = input("Is the snack available? (yes/no): ").lower()
    
    snack_inventory[snack_id] = {
        "name": snack_name,
        "price": price,
        "available": available == "yes",
    }
    print(f"Snack '{snack_name}' added to the inventory.")

# Function to remove a snack from the inventory
def remove_snack():
    snack_id = input("Enter snack ID to remove: ")
    if snack_id in snack_inventory:
        del snack_inventory[snack_id]
        print(f"Snack with ID '{snack_id}' removed from the inventory.")
    else:
        print(f"Snack with ID '{snack_id}' not found in the inventory.")

# Function to update the availability of a snack
def update_availability():
    snack_id = input("Enter snack ID to update availability: ")
    if snack_id in snack_inventory:
        available = input("Is the snack available? (yes/no): ").lower()
        snack_inventory[snack_id]["available"] = available == "yes"
        print(f"Availability of snack '{snack_inventory[snack_id]['name']}' updated.")
    else:
        print(f"Snack with ID '{snack_id}' not found in the inventory.")

# Function to record a sale
def record_sale():
    snack_id = input("Enter snack ID sold: ")
    if snack_id in snack_inventory:
        if snack_inventory[snack_id]["available"]:
            quantity = int(input("Enter quantity sold: "))
            if snack_id in sales_record:
                sales_record[snack_id] += quantity
            else:
                sales_record[snack_id] = quantity
            print(f"Sale recorded for snack '{snack_inventory[snack_id]['name']}'.")
            snack_inventory[snack_id]["available"] = False
        else:
            print(f"Snack '{snack_inventory[snack_id]['name']}' is not available.")
    else:
        print(f"Snack with ID '{snack_id}' not found in the inventory.")

# Function to view all snacks in the inventory
def view_all_snacks():
    if not snack_inventory:
        print("The inventory is empty.")
    else:
        print("Snack ID  |  Snack Name  |  Price  |  Availability")
        print("-" * 50)
        for snack_id, snack_info in snack_inventory.items():
            print(f"{snack_id:<10} | {snack_info['name']:<12} | {snack_info['price']:<6.2f} | {'Yes' if snack_info['available'] else 'No'}")

# Main loop for user interaction
while True:
    print("\nMumbai Munchies Inventory Management System")
    print("1. Add a snack to the inventory")
    print("2. Remove a snack from the inventory")
    print("3. Update snack availability")
    print("4. Record a sale")
    print("5. View all snacks")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_snack()
    elif choice == "2":
        remove_snack()
    elif choice == "3":
        update_availability()
    elif choice == "4":
        record_sale()
    elif choice == "5":
        view_all_snacks()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please choose a valid option.")




# # Main loop for user interaction
# while True:
#     print("\nMumbai Munchies Inventory Management System")
#     print("1. Add a snack to the inventory")
#     print("2. Remove a snack from the inventory")
#     print("3. Update snack availability")
#     print("4. Record a sale")
#     print("5. View All Snacks")
#     print("6. Exit")
    
#     choice = input("Enter your choice: ")
    
#     if choice == "1":
#         add_snack()
#     elif choice == "2":
#         remove_snack()
#     elif choice == "3":
#         update_availability()
#     elif choice == "4":
#         record_sale()
#     elif choice == "5":
#         view_snacks()
#     elif choice == "6":
#         break
#     else:
#         print("Invalid choice. Please choose a valid option.")

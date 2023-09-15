snackInventory={}
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
        print("Invalid choice. Please choose a valid option.")
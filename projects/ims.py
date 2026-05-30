inventory = {}

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))
    inventory[name] = quantity
    print(f"Added {quantity} of {name} to inventory.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for name, quantity in inventory.items():
            print(f"{name}: {quantity}")

def remove_item():
    name = input("Enter item name to remove: ")
    if name in inventory:
        del inventory[name]
        print(f"Removed {name} from inventory.")
    else:
        print(f"{name} not found in inventory.")
        
def update_item():
    name = input("Enter item name to update: ")
    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name] = quantity
        print(f"Updated {name} quantity to {quantity}.")
    else:
        print(f"{name} not found in inventory.")
        
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Remove Item")
        print("4. Update Item")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            update_item()
        elif choice == '5':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
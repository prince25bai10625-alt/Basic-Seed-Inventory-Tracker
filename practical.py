# This script uses only fundamental Python structures (lists, dictionaries, loops)
# and requires no external libraries.

# --- 1. Initial Inventory Data ---
# This list holds the seed details: name, quantity (how many left), and price (money).
seed_inventory = [
    {"name": "Hybrid Maize (Red)", "quantity": 550, "price": 45.00},
    {"name": "Local Wheat (Sona)", "quantity": 1200, "price": 32.50},
    {"name": "Paddy (Basmati 1509)", "quantity": 80, "price": 60.75}, # Low stock
    {"name": "Mung Bean (Summer)", "quantity": 300, "price": 70.00},
]

def display_inventory():
    """
    Displays the current inventory details: Name, Quantity Left, and Price.
    """
    if not seed_inventory:
        print("\n--- Inventory is Empty ---")
        return

    print("\n" + "="*60)
    print("       RURAL SEED DISTRIBUTION CENTER INVENTORY")
    print("="*60)
    # Print the column headers
    print(f"{'No.':<4}{'Seed Name':<30}{'Quantity Left':<15}{'Price (₹)':<10}")
    print("-" * 60)

    total_value = 0
    total_stock = 0

    for i, seed in enumerate(seed_inventory):
        quantity = seed.get('quantity', 0)
        price = seed.get('price', 0.0)

        total_value += quantity * price
        total_stock += quantity

        # Display the formatted inventory item
        print(f"{i+1:<4}{seed['name']:<30}{quantity:<15}{price:<10.2f}")

        # Simple stock status alerts
        if quantity < 100 and quantity > 0:
             print(f"  *** LOW STOCK WARNING for {seed['name']} ***")
        elif quantity == 0:
             print(f"  *** OUT OF STOCK: {seed['name']} ***")


    print("-" * 60)
    print(f"Total Stock: {total_stock} units")
    print(f"Estimated Total Value: ₹{total_value:,.2f}")
    print("="*60)

def add_new_seed():
    """
    Adds a new seed variety to the inventory list.
    """
    print("\n--- Add New Seed Variety ---")
    name = input("Enter seed name: ").strip()
    
    # Simple check to prevent duplicates
    if any(seed.get('name', '').lower() == name.lower() for seed in seed_inventory):
        print(f"Error: '{name}' already exists.")
        return

    try:
        # Input validation for numbers
        quantity = int(input("Enter initial stock quantity (units): "))
        price = float(input("Enter price per unit (₹): "))
        
        if quantity < 0 or price < 0:
            print("Error: Quantity and price must be positive.")
            return

        new_seed = {
            "name": name, 
            "quantity": quantity, 
            "price": price
        }
        seed_inventory.append(new_seed)
        print(f"\nSuccessfully added '{name}'.")
    except ValueError:
        print("Invalid input. Please enter a whole number for quantity and a valid number for price.")

def update_stock():
    """
    Updates the quantity of an existing seed variety.
    """
    display_inventory()
    if not seed_inventory:
        return

    try:
        # Get the number corresponding to the seed you want to change
        choice = int(input("\nEnter the number of the seed to update stock: "))
        
        if 1 <= choice <= len(seed_inventory):
            seed_index = choice - 1
            seed = seed_inventory[seed_index]
            
            print(f"\nCurrently updating: {seed['name']} (Stock: {seed['quantity']})")
            
            # Get the change amount (positive to add, negative to remove)
            adjustment = int(input("Enter quantity to ADD (e.g., 50) or REMOVE (e.g., -20): "))
            
            new_quantity = seed['quantity'] + adjustment
            
            if new_quantity < 0:
                print(f"Error: Cannot remove {abs(adjustment)} units. Only {seed['quantity']} units are in stock.")
                return

            seed_inventory[seed_index]['quantity'] = new_quantity
            print(f"\nStock updated for {seed['name']}. New quantity: {new_quantity}.")
        else:
            print("Invalid number selected.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

def main_menu():
    """
    Runs the main interactive console menu loop.
    """
    while True:
        display_inventory()
        
        print("\n--- Inventory Menu ---")
        print("1. Add New Seed Variety")
        print("2. Update/Adjust Stock Quantity (Add or Sell)")
        print("3. Refresh/View Inventory (Redisplays table)")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_new_seed()
        elif choice == '2':
            update_stock()
        elif choice == '3':
            # Display is handled by the start of the loop
            print("\nInventory refreshed.")
        elif choice == '4':
            print("Exiting Inventory Tracker. Goodbye!")
            break # Exit the while loop
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            
        # Pause to read the output before the screen refreshes
        if choice != '4':
            input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main_menu()

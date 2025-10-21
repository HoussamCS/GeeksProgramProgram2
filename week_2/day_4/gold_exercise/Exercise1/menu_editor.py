from menu_manager import MenuManager

def load_manager():
    return MenuManager()

def add_item_to_menu(manager):
    name = input("Enter item name: ")
    try:
        price = float(input("Enter item price: "))
        manager.add_item(name, price)
        print("✅ Item added successfully!")
    except ValueError:
        print("❌ Invalid price. Please enter a number.")

def remove_item_from_menu(manager):
    name = input("Enter the item name to remove: ")
    if manager.remove_item(name):
        print("✅ Item removed successfully!")
    else:
        print("❌ Item not found in the menu.")

def show_restaurant_menu(manager):
    manager.show_menu()

def show_user_menu():
    print("""
    🍴 Exercise Menu Manager 🍴
    1. Show Menu
    2. Add Item
    3. Remove Item
    4. Save and Exit
    """)

def main():
    manager = load_manager()

    while True:
        show_user_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            show_restaurant_menu(manager)
        elif choice == "2":
            add_item_to_menu(manager)
        elif choice == "3":
            remove_item_from_menu(manager)
        elif choice == "4":
            manager.save_to_file()
            print("👋 Exiting program. Menu saved.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import json

class MenuManager:
    def __init__(self, file_path="restaurant_menu.json"):
        self.file_path = file_path
        try:
            with open(self.file_path, "r") as file:
                self.menu = json.load(file)
        except FileNotFoundError:
            print("Menu file not found. Starting with an empty menu.")
            self.menu = {"items": []}

    def add_item(self, name, price):
        """Add a new item to the menu (not saved yet)."""
        self.menu["items"].append({"name": name, "price": price})

    def remove_item(self, name):
        """Remove an item by name. Returns True if successful."""
        for item in self.menu["items"]:
            if item["name"].lower() == name.lower():
                self.menu["items"].remove(item)
                return True
        return False

    def save_to_file(self):
        """Save the menu to the JSON file."""
        with open(self.file_path, "w") as file:
            json.dump(self.menu, file, indent=4)
        print("✅ Menu saved successfully to file.")

    def show_menu(self):
        """Display the restaurant menu."""
        print("\n🍽️ Restaurant Menu:")
        for item in self.menu["items"]:
            print(f"- {item['name']} : {item['price']} MAD")

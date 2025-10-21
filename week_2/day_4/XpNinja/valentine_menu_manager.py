import re
import json

class ValentineMenuManager:
    def __init__(self, file_path="restaurant_menu.json"):
        self.file_path = file_path
        try:
            with open(self.file_path, "r") as file:
                self.menu = json.load(file)
        except FileNotFoundError:
            self.menu = {"items": [], "valentine_items": []}

    def validate_name(self, name):
        # Must start with capital V, each word capitalized except connection words
        if not name.startswith("V"):
            return False
        if not re.match(r"^[A-Za-z\s\-]+$", name):  # No numbers
            return False
        if name.count("e") < 2:  # Must contain at least two 'e'
            return False
        return True

    def validate_price(self, price):
        # Must match format: XX,14 (e.g., 24,14)
        return bool(re.match(r"^\d{2},14$", price))

    def add_valentine_item(self, name, price):
        if self.validate_name(name) and self.validate_price(price):
            self.menu["valentine_items"].append({"name": name, "price": price})
            print(f"✅ '{name}' added to Valentine’s menu!")
        else:
            print("❌ Invalid item. Please follow the rules!")

    def save_to_file(self):
        with open(self.file_path, "w") as file:
            json.dump(self.menu, file, indent=4)
        print("💾 Valentine menu saved successfully!")

    def show_heart(self):
        print("\n💖 Valentine’s Heart 💖")
        heart = [
            "  ***     ***  ",
            " *****   ***** ",
            "******* *******",
            " ************* ",
            "  ***********  ",
            "   *********   ",
            "    *******    ",
            "     *****     ",
            "      ***      ",
            "       *       "
        ]
        for line in heart:
            print(line)

    def show_valentine_menu(self):
        self.show_heart()
        print("\n🌹 Valentine’s Menu 🌹")
        for item in self.menu["valentine_items"]:
            print(f"- {item['name']} : {item['price']} MAD")

if __name__ == "__main__":
    manager = ValentineMenuManager()

    name = input("Enter the Valentine item name: ")
    price = input("Enter the price (format XX,14): ")

    manager.add_valentine_item(name, price)
    manager.save_to_file()
    manager.show_valentine_menu()

import math
import random

# Exercice1: Geometry, Circle Area and Perimeter
print("Exercice 1: Circle Area and Perimeter")

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    # Computeing perimeter (circumference)
    def perimeter(self):
        return 2 * math.pi * self.radius

    # Computing area
    def area(self):
        return math.pi * self.radius ** 2

    # printing geometric definition
    def definition(self):
        print("A circle is a shape consisting of all points in a plane that are at a given distance from a fixed point, the center.")

# Example 
c = Circle(5)
print(f"Perimeter: {c.perimeter():.2f}")
print(f"Area: {c.area():.2f}")
c.definition()



# Exercice 2: Custom List Class
print("\nExercice 2: Custom List Class")

class MyList:
    def __init__(self, letters):
        self.letters = letters

    # Returnning reversed list
    def reversed_list(self):
        return self.letters[::-1]

    # Returning sorted list
    def sorted_list(self):
        return sorted(self.letters)

    # Bonus: generate a random numbers list of same length
    def random_numbers_list(self):
        return [random.randint(0, 100) for _ in range(len(self.letters))]

# Example 
mylist = MyList(['a', 'd', 'b', 'c'])
print("Original:", mylist.letters)
print("Reversed:", mylist.reversed_list())
print("Sorted:", mylist.sorted_list())
print("Random numbers list:", mylist.random_numbers_list())





# Exercice 3: Restaurant Menu
print("\nExercice 3: Restaurant Menu")
class MenuManager:
    def __init__(self):
        # Initial menu: list of dictionaries
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    # Adding a new dish
    def add_item(self, name, price, spice, gluten):
        self.menu.append({"name": name, "price": price, "spice": spice, "gluten": gluten})
        print(f"{name} added to the menu.")

    # Updating an existing dish
    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                dish.update({"price": price, "spice": spice, "gluten": gluten})
                print(f"{name} updated successfully.")
                return
        print(f"{name} is not in the menu.")

    # Removing a dish
    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                print(f"{name} removed. Updated menu:")
                print(self.menu)
                return
        print(f"{name} is not in the menu.")

# Example 
if __name__ == "__main__":
    manager = MenuManager()
    manager.add_item("Pizza", 20, "A", True)
    manager.update_item("Salad", 19, "A", False)
    manager.remove_item("Hamburger")


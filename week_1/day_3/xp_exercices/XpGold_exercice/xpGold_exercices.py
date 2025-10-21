# Ecercice 1: Birthday Lookup
birthdays = {
    "Alice": "1990/05/12",
    "Bob": "1985/11/23",
    "Charlie": "1992/07/08",
    "Dana": "1988/02/14",
    "Eli": "1995/09/30"
}

# Welcome message
print("Welcome! You can look up the birthdays of the people in the list!")

# Ask user for a name
name = input("Enter the name of the person: ")

# Get and print birthday
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {name}")






# Ecercice 2: Birthdays
print("People in the list:", ", ".join(birthdays.keys()))

# Ask user for a name
name = input("Enter the name of the person: ")

# Check if the name exists
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {name}")





# Ecercice 3: Add a Birthday
new_name = input("Enter a person's name to add: ")
new_birthday = input(f"Enter {new_name}'s birthday (YYYY/MM/DD): ")

# Add to dictionary
birthdays[new_name] = new_birthday

# Show all names
print("Updated list of people:", ", ".join(birthdays.keys()))

# Ask the user to look up a birthday
lookup_name = input("Enter the name of the person to look up: ")

if lookup_name in birthdays:
    print(f"{lookup_name}'s birthday is on {birthdays[lookup_name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {lookup_name}")




# Exercice 4: Fruit shop

# Part 1: Print items and prices
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for item, price in items.items():
    print(f"The price of {item} is ${price}.")

# Part 2: Calculate total cost in stock
items_stock = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

total_cost = 0
for item, info in items_stock.items():
    cost = info["price"] * info["stock"]
    total_cost += cost

print(f"The total cost to buy everything in stock is: ${total_cost}")


# Copying string and convert to list
cars_str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
cars_list = [car.strip() for car in cars_str.split(",")]

# Printing how many manufacturers
print(f"There are {len(cars_list)} manufacturers in the list.")

# Printing list in reverse (Z-A)
print("Manufacturers in descending order (Z-A):", sorted(cars_list, reverse=True))

# Counting names with 'o'
count_o = sum(1 for car in cars_list if 'o' in car or 'O' in car)
print(f"Number of manufacturers with the letter 'o': {count_o}")

# Counting names without 'i'
count_no_i = sum(1 for car in cars_list if 'i' not in car and 'I' not in car)
print(f"Number of manufacturers without the letter 'i': {count_no_i}")

#Bonus Part 1: Removing duplicates
cars_with_duplicates = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
cars_unique = list(set(cars_with_duplicates))
print("Companies without duplicates:", ", ".join(cars_unique))
print(f"Number of companies now: {len(cars_unique)}")

# --- Bonus Part 2: Ascending order with reversed letters ---
cars_sorted = sorted(cars_unique)
cars_reversed_letters = [car[::-1] for car in cars_sorted]
print("Ascending order with letters reversed:", cars_reversed_letters)

#Ecercice 1   

print("Exercise 1: Favorite numbers")
# Creating a set of favorite numbers
my_fav_numbers = {7, 14, 21}
# Adding two new numbers
my_fav_numbers.add(28)
my_fav_numbers.add(35)
# Removing the last number added
last_added = list(my_fav_numbers)[-1]
my_fav_numbers.remove(last_added)
# Friend's favorite numbers
friend_fav_numbers = {3, 9, 14}
# Concatenate using union   
our_fav_numbers = my_fav_numbers.union(
    
)

print("My favorite numbers:", my_fav_numbers)
print("Friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)


# Exercice 2   

print("\nExercise 2: Tuple")
my_tuple = (1, 2, 3, 4)

new_tuple = my_tuple + (5, 6)
print(new_tuple)  


# Exercice 3
print("\nExercise 3: List")   

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print("Apples count:", basket.count("Apples"))
basket.clear()
print("Final basket:", basket)


# Exercice 4
print("\nExercise 4: Floats")

numbers = []
x = 1.5
while x <= 5:
    numbers.append(x)
    x += 0.5
print(numbers)


# Exercice 5
print("\nExercise 5: For loop")
# Print all numbers from 1 to 20
for i in range(1, 21):
    print(i)

# Print numbers where index is even
print("Even index numbers:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Exercice 6
print("\nExercise 6: While loop")   
my_name = "Houssam"

while True:
    user_name = input("Enter your name: ")
    if user_name == my_name:
        print("Hey, that's my name ")
        break

# Exercice 7
print("\nExercise 7: Favorite fruits")
fruits = input("Enter your favorite fruits (separated by spaces): ").split()
chosen_fruit = input("Enter a fruit: ")

if chosen_fruit in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exercice 8
print("\nExercise 8: Who ordered a pizza?")
toppings = []
price = 10  # base price

while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

price += len(toppings) * 2.5
print("Your toppings:", toppings)
print(f"Total price: ${price}")

# Exercice 9
print("\nExercise 9: Cinemax tickets")

total_cost = 0
ages = input("Enter ages of family members (separated by spaces): ").split()
ages = [int(age) for age in ages]

for age in ages:
    if age < 3:
        total_cost += 0
    elif 3 <= age <= 12:
        total_cost += 10
    else:
        total_cost += 15

print("Total ticket cost:", total_cost)

# Bonus: restricted movie 16–21
attendees = []
for age in ages:
    if 16 <= age <= 21:
        attendees.append(age)

print("Allowed attendees (ages 16-21):", attendees)

# Exercice 10
print("\nExercise 10: Sandwich orders")
sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
finished_sandwiches = []

print("Sorry, we are out of Pastrami!")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("Finished sandwiches:", finished_sandwiches)


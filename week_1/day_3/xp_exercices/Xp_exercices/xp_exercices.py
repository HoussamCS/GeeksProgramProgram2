# Exercise 1: Converting Lists into Dictionaries
print("***Exercise 1: Converting Lists into Dictionaries***")

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = dict(zip(keys, values))
print(result)

# Exercise 2:  Cinemax #2
print("\nExercise 2: Cinemax #2")
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for membre, age in family.values():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
  
print(f"Ticket price for each family member: {cost}")
total_cost += cost  
   
print(f"Total cost for the family is: ${total_cost}")

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for member, age in family.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    
    print(f"Ticket price for {member} (age {age}): ${cost}")
    total_cost += cost

print(f"Total cost for the family is: ${total_cost}")


#Exercice 3 : Zara
print("\nExercise 3: Zara")
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": "men, women, children, home",
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]}
}

brand["number_stores"] = 2

print(f"Zara's clients are: {brand['type_of_clothes']}")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")


brand.pop("creation_date")

print(brand["international_competitors"][-1])

print(brand["major_color"]["US"])

print(len(brand))

print(brand.keys())

# Bonus
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 7000
}

brand.update(more_on_zara)
print(brand)


#Bonus Exercice3 
more_on_zara = {
"creation_date": 1975,  
"number_stores": 7000
}

brand.update(more_on_zara)
print(brand)

#Exercise 4: Disney Characters
print("\nExercise 4: Disney Characters")
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

#1. Dictionary that maps characters to their indices:
dictionary1 = {user: index for index, user in enumerate(users)}
print(dictionary1)

#2. Create a dictionary that maps indices to characters:
dictionary2={index: user for index, user in enumerrate(users)}
print(dictionary2)

#3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
sorted_users = sorted(users)
dictionary3 = {user: index for index, user in enumerate(sorted_users)}
print(dictionary3)








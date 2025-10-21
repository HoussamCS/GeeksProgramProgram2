# Exercice 1 :What Are You Learning?
def display_message():
    print("I am learning about functions in Python.")

display_message()


# Exercice 2:Your Favorite Book?

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")


# Exercice 3 :Geography
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")


# Exercice4 :Random
import random

def guess_random(user_number):
    rand_number = random.randint(1, 100)
    if user_number == rand_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {rand_number}")

guess_random(50)  # Replace 50 with any number between 1-100

# Exercice 5 :Create Some Personalized Shirts!
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt()
make_shirt("medium")
make_shirt("small", "Custom message")
make_shirt(size="small", text="Hello!")


# Exercice 6 :Magicians
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    for i in range(len(names)):
        names[i] += " the Great"

make_great(magician_names)
show_magicians(magician_names)

# Exercise 7: Temperature Advice
import random

def get_random_temp():
    return random.uniform(-10, 40)

def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp:.1f} degrees Celsius.")
    
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 < temp <= 23:
        print("Nice weather.")
    elif 23 < temp <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")

main()


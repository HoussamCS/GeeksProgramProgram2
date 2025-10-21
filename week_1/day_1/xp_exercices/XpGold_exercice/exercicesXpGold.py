# Exercice 1: Hello World - I love Python
print("Exercice:  Hello World-I love Python")
for i in range(4):
    print("Hello world")
for i in range(4):
    print("I love python")


# Exercice 2: What is the Season
print("\nExercise 2: What is the Season")
month = int(input("Enter a month number (1-12): "))
if month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:
    print("Winter")

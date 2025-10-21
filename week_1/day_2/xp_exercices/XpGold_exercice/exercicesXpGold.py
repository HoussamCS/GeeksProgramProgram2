# Exercise 1: Concatenate lists (without +)
print("Exercise 1: Concatenate lists (without +)")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using extend() instead of +
list1.extend(list2)
print(list1)


# Exercise 2: Range of numbers
print("\nExercise 2: Range of numbers")
for number in range(1500, 2501):
    if number % 5 == 0 and number % 7 == 0:
        print(number)


# Exercise 3: Check the index
print("\nExercise 3: Check the index")
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter your name: ")

if user_name in names:
    print("Index:", names.index(user_name))
else:
    print("Name not found.")


# Exercise 4: Greatest Number
print("\nExercise 4: Greatest Number")
num1 = int(input("Input the 1st number: "))
num2 = int(input("Input the 2nd number: "))
num3 = int(input("Input the 3rd number: "))

print("The greatest number is:", max(num1, num2, num3))


# Exercise 5: The Alphabet
print("\nExercise 5: The Alphabet")
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")


# Exercise 6: Words and letters
print("\nExercise 6: Words and letters")
words = []
for i in range(7):
    word = input(f"Enter word {i+1}: ")
    words.append(word)

letter = input("Enter a single character: ")

for word in words:
    if letter in word:
        print(f"In '{word}', '{letter}' appears at index {word.index(letter)}")
    else:
        print(f"'{letter}' not found in '{word}'")


# Exercise 7: Min, Max, Sum
print("\nExercise 7: Min, Max, Sum")
numbers = list(range(1, 1_000_001))

print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))



# Exercise 8: List and Tuple
print("\nExercise 8: List and Tuple")

values = input("Enter comma-separated numbers: ")
list_values = values.split(",")
tuple_values = tuple(list_values)

print(list_values)
print(tuple_values)



# Exercise 9: Random number
print("\nExercise 9: Random number")
import random

wins = 0
losses = 0

while True:
    user_input = input("Enter a number from 1 to 9 (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break

    try:
        user_num = int(user_input)
        if not 1 <= user_num <= 9:
            print("Please enter a number between 1 and 9.")
            continue

        random_num = random.randint(1, 9)
        print("Computer chose:", random_num)

        if user_num == random_num:
            print("🎉 Winner!")
            wins += 1
        else:
            print("Better luck next time!")
            losses += 1
    except ValueError:
        print("Invalid input, please enter a number.")

print(f"🏁 Games won: {wins} | Games lost: {losses}")   
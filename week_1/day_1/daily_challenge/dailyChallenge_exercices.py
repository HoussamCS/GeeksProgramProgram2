# Part 1
import random


print("***Part 1***")

string = input("Enter a string: ")

# Part 2
if len(string) == 10 :
    print("Perfect string")
if len(string) < 10 :
    print("short string")
else:
    print("long string")

# Part 3
print("***Part 3***")
print("The first caracter is:" + string[0])
print("the last caracter is:" + string[-1])

# Part 4
print("***Part 4***")

if len(string) == 10:
    print("\nBuilding the string:")
    for i in range(1, len(string) + 1):
        print(string[:i])

# Part 5
print("***Part 5***")
print("\nJumbled string (Bonus):")
if len(string) == 10:
    jumbled = list(string)
    random.shuffle(jumbled)
    print("\nJumbled string:", ''.join(jumbled))
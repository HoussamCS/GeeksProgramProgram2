 # Exercice : When will I retire ?

def get_age(year, month, day):
    current_year = 2025
    current_month = 10
    age = current_year - year
    if month > current_month:
        age -= 1
    return age

def can_retire(gender, date_of_birth):
    year, month, day = map(int, date_of_birth.split("/"))
    age = get_age(year, month, day)
    if gender.lower() == "m":
        return age >= 67
    elif gender.lower() == "f":
        # Women born after April 1947
        if year > 1947 or (year == 1947 and month > 4):
            return age >= 62
        else:
            return age >= 65  # older women retire at 65
    else:
        return False

gender = input("Enter your gender (m/f): ")
dob = input("Enter your date of birth (yyyy/mm/dd): ")
if can_retire(gender, dob):
    print("You can retire!")
else:
    print("You cannot retire yet.")


# Ecercice 2:Sum
def sum_pattern(x):
    total = int(str(x)) + int(str(x)*2) + int(str(x)*3) + int(str(x)*4)
    return total

num = int(input("Enter a number: "))
print("Result:", sum_pattern(num))


# Ecercice 3: Double Dice Simulation
import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    count = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        count += 1
        if dice1 == dice2:
            return count

def main():
    results = []
    for _ in range(100):
        results.append(throw_until_doubles())
    total_throws = sum(results)
    average_throws = total_throws / len(results)
    print(f"Total throws to reach 100 doubles: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

main()

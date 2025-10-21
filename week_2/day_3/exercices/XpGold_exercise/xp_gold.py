# Exercise 1 : Upcoming Holiday
print("Exercise 1 : Upcoming Holiday")
from datetime import date, timedelta
import holidays

def next_holiday():
    today = date.today()
    ma_holidays = holidays.Morocco(years=today.year)

    # if all holidays of current year passed, check next year
    if max(ma_holidays.keys()) < today:
        ma_holidays = holidays.Morocco(years=today.year + 1)

    # find next holiday
    for h_date, h_name in sorted(ma_holidays.items()):
        if h_date >= today:
            days_left = (h_date - today).days
            print(f"Today's date: {today}")
            print(f"The next holiday is {h_name} in {days_left} days.")
            break

next_holiday()

# Exercise 2 : How Old Are You On Jupiter?
print("\nExercise 2 : How Old Are You On Jupiter?")
def age_on_planets(seconds):
    earth_year_seconds = 31557600
    planets = {
        'Earth': 1.0,
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132
    }

    for planet, ratio in planets.items():
        age = seconds / (earth_year_seconds * ratio)
        print(f"Your age on {planet}: {age:.2f} years")

age_on_planets(1000000000)

# Exercise 3 : Regular Expression 
import re

def return_numbers(text):
    numbers = re.findall(r'\d', text)
    return ''.join(numbers)

print(return_numbers('k5k3q2g5z6x9bn'))  # Output: 532569

#Exercise 4 : Regular Expression2
print("\nExercise 4 : Regular Expression #2")
import re

def validate_name(name):
    pattern = r'^[A-Z][a-zA-Z]+ [A-Z][a-zA-Z]+$'
    if re.match(pattern, name):
        print(" Valid name!")
    else:
        print(" Invalid name. Make sure to use only letters and one space, both names capitalized.")


validate_name("John Doe")  
validate_name("john doe")  


#Exercise 5 : Python Password Generato
print("\nExercise 5 : Python Password Generator")
import random
import string

def generate_password():
    while True:
        try:
            length = int(input("Enter password length (6–30): "))
            if 6 <= length <= 30:
                break
            else:
                print("❌ Must be between 6 and 30.")
        except ValueError:
            print("❌ Please enter a valid number.")

    chars = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            break

    print(f"✅ Your password: {password}\nKeep it safe!")

generate_password()

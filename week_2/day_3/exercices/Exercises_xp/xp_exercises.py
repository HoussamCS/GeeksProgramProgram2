# Exercice 1:
print("Exercice 1:")
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}{'s' if self.amount != 1 else ''}"

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return int(self.amount)

    def __add__(self, other):
        if isinstance(other, Currency):
            if other.currency != self.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        elif isinstance(other, (int, float)):
            return self.amount + other
        else:
            raise TypeError("Unsupported addition type")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if other.currency != self.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, (int, float)):
            self.amount += other
        else:
            raise TypeError("Unsupported addition type")
        return self


# 🧪 Test Code
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)           
print(int(c1))      
print(repr(c1))     
print(c1 + 5)       
print(c1 + c2)      
print(c1)           
c1 += 5
print(c1)           
c1 += c2
print(c1)           
print(c1 + c3)      


# Exercice 2:
print("\nExercice 2:")
def add_numbers(a, b):
    print("Sum:", a + b)


# Exercice 3:Random string
print("\nExercice 3: Random string")
import string
import random

letters = string.ascii_letters  
random_string = ''.join(random.choice(letters) for _ in range(5))
print("Random string:", random_string)


#Exercise 4: Current Date
print("\nExercise 4: Current Date")
from datetime import date

def show_current_date():
    today = date.today()
    print("Today's date:", today)

show_current_date()

# Exercise 5: Time Until January 1st
print("\nExercise 5: Time Until January 1st")
from datetime import datetime

def time_until_new_year():
    now = datetime.now()
    next_year = datetime(year=now.year + 1, month=1, day=1)
    delta = next_year - now
    print("Time until New Year:", delta)

time_until_new_year()

#Exercise 6: Birthday Minutes
print("\nExercise 6: Birthday Minutes")
from datetime import datetime

def minutes_lived(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.now()
    lived = now - birthdate
    minutes = lived.total_seconds() / 60
    print(f"You have lived approximately {int(minutes):,} minutes.")

minutes_lived("2000-05-15")


# Exercise 7: Faker Module
print("\nExercise 7: Faker Module")
from faker import Faker

fake = Faker()
users = []

def generate_users(n):
    for _ in range(n):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)
    return users

fake_users = generate_users(5)
for user in fake_users:
    print(user)









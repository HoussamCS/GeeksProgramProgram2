from datetime import datetime

birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")
birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")

today = datetime.today()

age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Number of candles = last digit of age
candles = age % 10
if candles == 0:
    candles = 10 

# Building the cake top with candles
cake_top = " " * 3 + "i" * candles + " " * 3

cake = f"""
   {cake_top}
  |:H:a:p:p:y:|
__|___________|__
^^^^^^^^^^^^^^^^^
|:B:i:r:t:h:d:a:y:|
|_________________|
~~~~~~~~~~~~~~~~~~~
"""

# Checking for leap year
year = birthdate.year
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(cake)
if is_leap:
    print("🎉 It's a leap year! You get TWO cakes! 🎉")
    print(cake)

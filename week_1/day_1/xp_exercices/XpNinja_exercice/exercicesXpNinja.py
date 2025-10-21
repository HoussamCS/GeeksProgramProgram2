# Exercice 3 :Predict the output of each line
print("Exercice 3: Predict the output of each line")

print(3 <= 3 < 9)                #  True 
print(3 == 3 == 3)               #  True 
print(bool(0))                   #  False 
print(bool(5 == "5"))            #  False 
print(bool(4 == 4) == bool("4" == "4"))  #  True
print(bool(bool(None)))          #  False 

x = (1 == True)                  #  True 
y = (1 == False)                 #  False
a = True + 4                     #  5 (True = 1)
b = False + 10                   #  10 (False = 0)

print("x is", x)  # x is True
print("y is", y)  # y is False
print("a:", a)    # a: 5
print("b:", b)    # b: 10


# Exercice 4 :# Exercice 3 :Predict the output of each line
print("\nExercise 4: Predict the output of each line")

my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(len(my_text))  #  Counts all characters including spaces and newlines



# Exercice 5 : The longest sentence without the letter 'A'
print("\nExercise 5: The longest sentence without the letter 'A'") 

longest_sentence = ""

while True:
    sentence = input("Enter the longest sentence you can without the letter 'A': ")

    if 'a' in sentence.lower():
        print(" Your sentence contains the letter 'A'. Try again!")
        continue

    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("🎉 Congratulations! You set a new record!")
    else:
        print("Keep trying to beat your record!")

    # Optional stop condition
    stop = input("Do you want to stop? (yes/no): ").lower()
    if stop == "yes":
        print(f"🏁 Your longest valid sentence was: \"{longest_sentence}\"")
        break





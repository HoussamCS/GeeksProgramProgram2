
import random

# Exercise 1: Random Sentence Generator
print("Exercise 1: Random Sentence Generator")
def get_words_from_file(file_path):
    """Reads words from a text file and returns them as a list."""
    try:
        with open(file_path, "r") as file:
            words = file.read().split()
            return words
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def get_random_sentence(length):
    """Generates a random sentence of a given length."""
    words = get_words_from_file("words.txt")  # make sure you have a 'words.txt' file
    if not words:
        return "No words available to generate a sentence."
    
    sentence_words = [random.choice(words) for _ in range(length)]
    sentence = " ".join(sentence_words).lower()
    return sentence

def main():
    print("Welcome to the Random Sentence Generator!")
    print("This program will generate a random sentence of your chosen length.")
    
    try:
        length = int(input("Enter the desired sentence length (2–20): "))
        
        if 2 <= length <= 20:
            sentence = get_random_sentence(length)
            print("\nYour random sentence is:")
            print(sentence)
        else:
            print("Error: Please enter a number between 2 and 20.")
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()



# Exercise 2: Working with JSON
print("\nExercise 2: Working with JSON")
import json

# Step 1: Load the JSON string
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Parsing the JSON string into a Python dictionary
data = json.loads(sampleJson)

# Accessing the nested “salary” key
salary = data["company"]["employee"]["payable"]["salary"]
print("Employee Salary:", salary)

# Adding the “birth_date” key
data["company"]["employee"]["birth_date"] = "1990-05-15"

# Saving the JSON to a file
with open("employee_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("\nModified JSON saved successfully as 'employee_data.json'")

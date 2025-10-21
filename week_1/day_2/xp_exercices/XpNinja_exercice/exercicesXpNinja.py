import math, random

# Ecercice 1: Compute Q based on user input
print("Exercise 1: Compute Q based on user input")
C = 50
H = 30

# Ask the user for input
D_values = input("Enter comma-separated numbers: ").split(',')

results = []
for D in D_values:
    Q = round(math.sqrt((2 * C * int(D)) / H))
    results.append(str(Q))

print(",".join(results))


# Exercise 2: List integers
print("\nExercise 2: List integers")
numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

# 2a: Print list in one line
print("List:", numbers)

# 2b: Sorted descending
print("Descending:", sorted(numbers, reverse=True))

# 2c: Sum of all numbers
print("Sum:", sum(numbers))

# 3: First and last numbers
print("First and last:", [numbers[0], numbers[-1]])

# 4: Numbers > 50
print("Greater than 50:", [n for n in numbers if n > 50])

# 5: Numbers < 10
print("Smaller than 10:", [n for n in numbers if n < 10])

# 6: Numbers squared
print("Squared:", [n**2 for n in numbers])

# 7: Unique numbers
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)
print("Count of unique numbers:", len(unique_numbers))

# 8: Average
print("Average:", sum(numbers)/len(numbers))

# 9: Largest
print("Largest:", max(numbers))

# 10: Smallest
print("Smallest:", min(numbers))



# Bonus part of exercice 2 
count = random.randint(50, 100)
numbers = [random.randint(-100, 100) for _ in range(count)]

print(f"Generated {len(numbers)} numbers")
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers)/len(numbers))



# Exercise 3: Text Analysis
print("\nExercise 3: Text Analysis")

paragraph = """Python is a widely used high-level programming language for general-purpose programming.
Created by Guido van Rossum and first released in 1991, Python emphasizes code readability.
Its syntax allows programmers to express concepts in fewer lines of code than would be possible in other languages."""

# Character count
char_count = len(paragraph)

# Sentence count
sentences = paragraph.split(".")
sentences = [s for s in sentences if s.strip() != ""]
sentence_count = len(sentences)

# Word count
words = paragraph.split()
word_count = len(words)

# Unique words
unique_words = set(words)
unique_word_count = len(unique_words)

# Bonus: Non-whitespace characters
non_whitespace = len(paragraph.replace(" ", "").replace("\n", ""))

# Bonus: Average words per sentence
avg_words_per_sentence = round(word_count / sentence_count, 2)

# Bonus: Non-unique words
non_unique_count = word_count - unique_word_count

print(f"Characters: {char_count}")
print(f"Sentences: {sentence_count}")
print(f"Words: {word_count}")
print(f"Unique words: {unique_word_count}")
print(f"Non-whitespace characters: {non_whitespace}")
print(f"Average words per sentence: {avg_words_per_sentence}")
print(f"Non-unique words: {non_unique_count}")


# Exercise 4: Word Frequency
print("\nExercise 4: Word Frequency")


text = input("Enter a sentence: ")

words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word, count in sorted(frequency.items()):
    print(f"{word}:{count}")




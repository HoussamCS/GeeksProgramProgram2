# Challenge 1: Sorting Words Alphabetically
print("Challenge 1: Sort words alphabetically")
words_input = input("Enter words separated by commas: ")  

# Splitting the string into a list
words_list = words_input.split(',')

# Sorting the list alphabetically
words_list.sort()

# Joining the sorted list back into a string
sorted_words = ','.join(words_list)

# Printing the result
print(sorted_words)



# Challenge 2:Longest Word in a Sentence
print("\nChallenge 2: Find the longest word in a sentence")
def longest_word(sentence):
    # Splitting the sentence into words
    words = sentence.split()
    
    # Initializing variables
    max_length = 0
    longest = ""

    # Iterating and comparing lengths
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest = word

    # Returning the longest word
    return longest

# Example runs
print(longest_word("Margaret's toy is a pretty doll."))  # Margaret's
print(longest_word("A thing of beauty is a joy forever."))  # forever.
print(longest_word("Forgetfulness is by all means powerless!"))  # Forgetfulness


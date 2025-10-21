# Exercice 1 : whats your name 

def get_full_name(first_name, last_name, middle_name=""):
    if middle_name:
        return f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"
    else:
        return f"{first_name.capitalize()} {last_name.capitalize()}"

# Examples
print(get_full_name("john", "lee", "hooker"))  # John Hooker Lee
print(get_full_name("bruce", "lee"))           # Bruce Lee



# Exercice 2: From English to Morse

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

def english_to_morse(text):
    text = text.upper()
    return ' '.join(MORSE_CODE_DICT.get(c, '/') if c != " " else "/" for c in text)

def morse_to_english(code):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    words = code.split(" / ")
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_words.append(''.join(reverse_dict.get(letter, '') for letter in letters))
    return ' '.join(decoded_words)

# Example
print(english_to_morse("Hello World"))
print(morse_to_english(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."))


# Exercice 3: Boxe of stars
def box_printer(*args):
    max_length = max(len(word) for word in args)
    print("*" * (max_length + 4))
    for word in args:
        print(f"* {word.ljust(max_length)} *")
    print("*" * (max_length + 4))

# Example
box_printer("Hello", "World", "in", "reallylongword", "a", "frame")


# Exercice 4: Purpose of the code
def insertion_sort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)




"""Hangman – classic word-guessing game played in the terminal."""

import random

WORDS = [
    'correction', 'childish', 'beach', 'python', 'assertive',
    'interference', 'complete', 'share', 'credit card', 'rush', 'south',
]
word = random.choice(WORDS).lower()

guessed_letters = set()
wrong_guesses = 0
max_wrong = 6
word_display = ['*' if char != ' ' else ' ' for char in word]

# ASCII art for each stage of the hangman (0 = no mistakes, 6 = game over)
hangman_stages = [
    "",
    "  O  ",
    "  O  \n  |  ",
    "  O  \n /|  ",
    "  O  \n /|\\",
    "  O  \n /|\\\n / ",
    "  O  \n /|\\\n / \\",
]

while wrong_guesses < max_wrong and '*' in word_display:
    print("\nWord: " + ''.join(word_display))
    print("Guessed letters: " + ', '.join(sorted(guessed_letters)))
    print("Wrong guesses: " + str(wrong_guesses))
    print(hangman_stages[wrong_guesses])

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        for i, char in enumerate(word):
            if char == guess:
                word_display[i] = guess
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong!")

if '*' not in word_display:
    print("\nCongratulations! You guessed the word: " + word)
else:
    print("\nGame Over! The word was: " + word)
    print(hangman_stages[wrong_guesses])

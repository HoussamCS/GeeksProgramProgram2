
from anagram_checker import AnagramChecker

def clean_input(user_input):
    """Trim spaces and check if input is valid (single alphabetic word)."""
    word = user_input.strip()
    if " " in word:
        print("❌ Error: Please enter only one word.")
        return None
    if not word.isalpha():
        print("❌ Error: Please enter alphabetic characters only.")
        return None
    return word

def main():
    checker = AnagramChecker("words.txt")  # Path to your word list file

    while True:
        print("\n🔠 MENU:")
        print("1️⃣ Enter a word")
        print("2️⃣ Exit")
        choice = input("Choose an option: ").strip()

        if choice == "2":
            print("👋 Goodbye!")
            break
        elif choice == "1":
            user_input = input("Enter a word: ")
            word = clean_input(user_input)
            if not word:
                continue

            if not checker.is_valid_word(word):
                print(f"❌ '{word}' is not a valid English word.")
                continue

            anagrams = checker.get_anagrams(word)
            print("\n✨ RESULTS ✨")
            print(f"YOUR WORD: '{word.upper()}'")
            print("This is a valid English word.")
            if anagrams:
                print(f"Anagrams for your word: {', '.join(anagrams)}")
            else:
                print("No anagrams found.")
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

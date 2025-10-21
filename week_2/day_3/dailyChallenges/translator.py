def translate_to_english(french_words):
    translations = {
        "Bonjour": "Hello",
        "Au revoir": "Goodbye",
        "Bienvenue": "Welcome",
        "A bientôt": "See you soon"
    }
    return {word: translations.get(word, "Unknown") for word in french_words}
    
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
result = translate_to_english(french_words)

print(result)
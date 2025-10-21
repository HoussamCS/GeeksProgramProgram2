import string
import re

# -------------------------------
# Part I: Text Analysis
# -------------------------------
class Text:
    def __init__(self, text: str):
        self.text = text

    def word_frequency(self, word: str):
        """Return how many times a word appears in the text."""
        words = self.text.lower().split()
        count = words.count(word.lower())
        return count if count > 0 else None

    def most_common_word(self):
        """Return the most common word in the text."""
        words = self.text.lower().split()
        frequency = {}
        for w in words:
            frequency[w] = frequency.get(w, 0) + 1
        if not frequency:
            return None
        return max(frequency, key=frequency.get)

    def unique_words(self):
        """Return a list of unique words in the text."""
        words = self.text.lower().split()
        return list(set(words))

    @classmethod
    def from_file(cls, file_path: str):
        """Create a Text instance from a file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return cls(content)
        except FileNotFoundError:
            print("File not found.")
            return None


# -------------------------------
# Part II: Text Modification (Inheritance)
# -------------------------------
class TextModification(Text):
    def remove_punctuation(self):
        """Remove all punctuation from the text."""
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = self.text.translate(translator)
        return cleaned_text

    def remove_stop_words(self):
        """Remove common English stop words from the text."""
        stop_words = {
            'a', 'the', 'and', 'is', 'in', 'to', 'it', 'of', 'for', 'on',
            'with', 'as', 'at', 'this', 'that', 'an', 'be', 'by', 'from'
        }
        words = self.text.split()
        filtered = [word for word in words if word.lower() not in stop_words]
        return ' '.join(filtered)

    def remove_special_characters(self):
        """Remove all non-alphanumeric characters (except spaces)."""
        cleaned = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return cleaned


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    # Example Using a direct string
    sample_text = "Hello world! This is a simple text. Hello again, world!"
    text_obj = Text(sample_text)
    print("Word frequency of 'hello':", text_obj.word_frequency("hello"))
    print("Most common word:", text_obj.most_common_word())
    print("Unique words:", text_obj.unique_words())

    # Example Using the TextModification class
    mod_text = TextModification(sample_text)
    print("\n--- Text Cleaning ---")
    print("Without punctuation:", mod_text.remove_punctuation())
    print("Without stop words:", mod_text.remove_stop_words())
    print("Without special characters:", mod_text.remove_special_characters())

    

"""AnagramChecker – validates words and finds anagrams from a word-list file."""


class AnagramChecker:
    def __init__(self, word_list_file):
        """Load the word list file into memory."""
        with open(word_list_file, 'r') as f:
            self.word_list = [word.strip().lower() for word in f.readlines()]

    def is_valid_word(self, word):
        """Check if a word is a valid English word."""
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        """Return True if word1 and word2 are anagrams."""
        return sorted(word1.lower()) == sorted(word2.lower()) and word1.lower() != word2.lower()

    def get_anagrams(self, word):
        """Find all anagrams for the given word."""
        word = word.lower()
        return [w for w in self.word_list if self.is_anagram(word, w)]

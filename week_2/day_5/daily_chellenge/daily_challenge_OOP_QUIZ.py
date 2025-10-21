# --------------------------------------------
#  Exercise 1: OOP Questions and Answers
# --------------------------------------------

"""
1️
A class is a blueprint for creating objects. It defines attributes and methods.

2️ 
An instance is a specific object created from a class.

3️ 
Encapsulation restricts direct access to some of an object's components, protecting data integrity.

4️ 
Abstraction hides complex details and shows only essential features.

5️
Inheritance allows a class to derive attributes and methods from another class.

6️ 
Multiple inheritance allows a class to inherit from more than one parent class.

7️ 
Polymorphism allows objects of different classes to be treated the same way if they share method names.

8️ 
MRO defines the order in which Python looks for a method in a hierarchy of classes.
"""

# --------------------------------------------
# Exercise 2: Deck of Cards
# --------------------------------------------

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        """Shuffle the deck of 52 cards"""
        if len(self.cards) < 52:
            print("Rebuilding the deck before shuffling...")
            self.__init__()  # reset deck if incomplete
        random.shuffle(self.cards)
        print("Deck shuffled!")

    def deal(self):
        """Deal a single card and remove it from the deck"""
        if len(self.cards) == 0:
            return "No cards left to deal!"
        return self.cards.pop()



if __name__ == "__main__":
    deck = Deck()
    print(f"Total cards before shuffle: {len(deck.cards)}")
    deck.shuffle()
    print("Dealing one card:", deck.deal())
    print(f"Cards left in deck: {len(deck.cards)}")

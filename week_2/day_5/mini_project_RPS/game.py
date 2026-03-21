# game.py – Rock Paper Scissors game logic
import random

class Game:
    ITEMS = ["rock", "paper", "scissors"]
    WIN_CONDITIONS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

    def __init__(self):
        self.items = self.ITEMS

    def get_user_item(self):
        """Prompt the user until a valid choice is entered."""
        while True:
            user_choice = input("Choose (rock/paper/scissors): ").strip().lower()
            if user_choice in self.items:
                return user_choice
            print("❌ Invalid choice! Please choose rock, paper, or scissors.")

    def get_computer_item(self):
        """Return a random computer choice."""
        return random.choice(self.items)

    def get_game_result(self, user_item, computer_item):
        """Return 'win', 'draw', or 'loss' based on the two choices."""
        if user_item == computer_item:
            return "draw"
        return "win" if self.WIN_CONDITIONS[user_item] == computer_item else "loss"

    def play(self):
        """Play one round of the game."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print("\n🪨 📄 ✂️ Game Results:")
        print(f"👉 You chose: {user_item}")
        print(f"🤖 Computer chose: {computer_item}")

        if result == "win":
            print("🎉 You WIN!")
        elif result == "loss":
            print("💀 You LOST!")
        else:
            print("😐 It's a DRAW!")

        return result

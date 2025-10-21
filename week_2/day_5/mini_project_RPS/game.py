# game.py
import random

class Game:
    def __init__(self):
        self.items = ["rock", "paper", "scissors"]

    def get_user_item(self):
        """Ask the user to select rock, paper, or scissors."""
        while True:
            user_choice = input("Choose (rock/paper/scissors): ").strip().lower()
            if user_choice in self.items:
                return user_choice
            print("❌ Invalid choice! Please choose rock, paper, or scissors.")

    def get_computer_item(self):
        """Randomly select the computer's choice."""
        return random.choice(self.items)

    def get_game_result(self, user_item, computer_item):
        """Determine and return 'win', 'draw', or 'loss'."""
        if user_item == computer_item:
            return "draw"

        win_conditions = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

        if win_conditions[user_item] == computer_item:
            return "win"
        else:
            return "loss"

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

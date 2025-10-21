from game import Game

def get_user_menu_choice():
    """Display the main menu and return user's choice."""
    print("\n🎮 Rock, Paper, Scissors Menu 🎮")
    print("1️⃣ Play a new game")
    print("2️⃣ Show scores")
    print("3️⃣ Quit")

    choice = input("Enter your choice (1/2/3): ").strip()
    if choice not in ["1", "2", "3"]:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
        return None
    return choice

def print_results(results):
    """Display the final game results."""
    print("\n📊 FINAL RESULTS 📊")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("🙏 Thanks for playing Rock Paper Scissors!")

def main():
    """Main program logic."""
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()
        if not choice:
            continue

        if choice == "1":
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == "2":
            print_results(results)

        elif choice == "3":
            print_results(results)
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    main()

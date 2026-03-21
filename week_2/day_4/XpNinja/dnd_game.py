"""D&D Character Generator – creates characters with randomly rolled stats and exports them."""

import random
import json

class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.attributes = self.generate_attributes()

    def roll_dice(self):
        # Roll 4d6 and drop the lowest die (standard D&D ability score method)
        dice = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(dice)[1:])

    def generate_attributes(self):
        stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        return {stat: self.roll_dice() for stat in stats}

    def __repr__(self):
        return f"Character({self.name}, Age: {self.age}, Stats: {self.attributes})"


class Game:
    def __init__(self):
        self.characters = []

    def start(self):
        num_players = int(input("How many players? "))
        for _ in range(num_players):
            name = input("Enter character name: ")
            age = int(input("Enter character age: "))
            char = Character(name, age)
            self.characters.append(char)
            print(f"\n✨ Created Character: {char}\n")

    def export_to_json(self, filename="dnd_characters.json"):
        data = [
            {"name": c.name, "age": c.age, "attributes": c.attributes}
            for c in self.characters
        ]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"💾 Saved all characters to {filename}")

    def export_to_txt(self, filename="dnd_characters.txt"):
        with open(filename, "w") as f:
            for c in self.characters:
                f.write(f"Character: {c.name} (Age: {c.age})\n")
                for stat, value in c.attributes.items():
                    f.write(f"  {stat}: {value}\n")
                f.write("\n")
        print(f"📜 Text file created: {filename}")


if __name__ == "__main__":
    game = Game()
    game.start()
    game.export_to_json()
    game.export_to_txt()

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}  # dictionary to store animal types and counts

    # AddING animals
    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    # GetTING formatted info
    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info

    # Returning sorted list of animal types
    def get_animal_types(self):
        return sorted(self.animals.keys())

    # Getting short info
    def get_short_info(self):
        animals_list = self.get_animal_types()
        formatted_animals = []
        for animal in animals_list:
            # Add 's' if count > 1
            if self.animals[animal] > 1:
                formatted_animals.append(animal + "s")
            else:
                formatted_animals.append(animal)
        # Join using commas and "and"
        if len(formatted_animals) > 1:
            short_info = ", ".join(formatted_animals[:-1]) + " and " + formatted_animals[-1]
        else:
            short_info = formatted_animals[0]
        return f"{self.name}'s farm has {short_info}."


# --- Test the class ---
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print("\nBonus info:")
print(macdonald.get_animal_types())
print(macdonald.get_short_info())

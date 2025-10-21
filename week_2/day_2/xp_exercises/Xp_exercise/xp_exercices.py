import random

# Exercice 1: Animaux de compagnie
print("Exercice 1: Animaux de compagnie")
class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Classe Siamese héritée de Cat
class Siamese(Cat):
    pass

# Liste d'instances
bengal = Bengal("Leo", 3)
chartreux = Chartreux("Milo", 4)
siamese = Siamese("Luna", 2)

all_cats = [bengal, chartreux, siamese]

# Instance Pets
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

sara_pets = Pets(all_cats)

#  Promenade
sara_pets.walk()


# Exercice 2: Chiens
print("\nExercice 2: Chiens")
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return "woof!"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if self_power > other_power:
            return f"{self.name} wins the fight!"
        elif self_power < other_power:
            return f"{other_dog.name} wins the fight!"
        else:
            return "It's a tie!"

# Création des instances
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 15)
dog3 = Dog("Max", 4, 25)

# Test des méthodes
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))


# Exercice 3: Chiens domestiqués
print("\nExercice 3: Chiens domestiqués")
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names = ", ".join([dog.name if isinstance(dog, Dog) else str(dog) for dog in args])
        print(f"{self.name} plays with {names}!")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

# Test PetDog
my_dog = PetDog("Fido", 2, 10)
friend_dog = PetDog("Buddy", 3, 12)
my_dog.train()
my_dog.play(friend_dog)
my_dog.do_a_trick()





# Exercice 4: classes familliales et personelles 
print("\nExercice 4: classes familliales et personelles ")
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("No member found with that name.")

    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, {member.age} years old")

# Test Family
smith_family = Family("Smith")
smith_family.born("Alice", 20)
smith_family.born("Bob", 16)
smith_family.family_presentation()
smith_family.check_majority("Alice")
smith_family.check_majority("Bob")

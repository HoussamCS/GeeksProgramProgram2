# Exercise 1: Temperature
print("Exercise 1: Temperature")
class Temperature:
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"{self.value:.2f} {self.__class__.__name__}"

class Celsius(Temperature):
    def to_kelvin(self):
        return Kelvin(self.value + 273.15)

    def to_fahrenheit(self):
        return Fahrenheit(self.value * 9/5 + 32)

class Kelvin(Temperature):
    def to_celsius(self):
        return Celsius(self.value - 273.15)

    def to_fahrenheit(self):
        return Fahrenheit((self.value - 273.15) * 9/5 + 32)

class Fahrenheit(Temperature):
    def to_celsius(self):
        return Celsius((self.value - 32) * 5/9)

    def to_kelvin(self):
        return Kelvin((self.value - 32) * 5/9 + 273.15)


# Example usage:
t_c = Celsius(25)
print(t_c)                     # 25.00 Celsius
print(t_c.to_kelvin())         # 298.15 Kelvin
print(t_c.to_fahrenheit())     # 77.00 Fahrenheit

t_f = Fahrenheit(32)
print(t_f.to_celsius())        # 0.00 Celsius
print(t_f.to_kelvin())         # 273.15 Kelvin



# Exercise 2: the Quantum Realm
print("\nExercise 2: In the Quantum Realm")
import random

class QuantumParticle:
    def __init__(self, x=0, p=0.0):
        self.x = x  # position
        self.p = p  # momentum
        self._spin = random.choice([0.5, -0.5])
        self.entangled_particle = None

    def __repr__(self):
        return f"QuantumParticle(x={self.x}, p={self.p:.3f}, spin={self._spin})"

    def disturb(self):
        self.x = random.randint(1, 10_000)
        self.p = random.random()
        print("⚡ Quantum Interferences!!")

    def position(self):
        self.disturb()
        pos = random.randint(1, 10_000)
        print(f"Measured position: {pos}")
        return pos

    def momentum(self):
        self.disturb()
        mom = random.random()
        print(f"Measured momentum: {mom:.4f}")
        return mom

    def spin(self):
        self.disturb()
        measured_spin = random.choice([0.5, -0.5])
        # if entangled, set the opposite spin
        if self.entangled_particle:
            self.entangled_particle._spin = -measured_spin
            print("🌀 Entangled spin adjusted automatically!")
        self._spin = measured_spin
        print(f"Measured spin: {measured_spin}")
        return measured_spin

    def entangle(self, other):
        if not isinstance(other, QuantumParticle):
            raise TypeError("Can only entangle with another QuantumParticle.")

        self.entangled_particle = other
        other.entangled_particle = self
        other._spin = -self._spin  # opposite spin correlation
        print("🧩 Spooky Action at a Distance !!")
        return f"Particle {id(self)} is now in quantum entanglement with Particle {id(other)}"


# ✅ Example usage:
p1 = QuantumParticle(x=1, p=5.0)
p2 = QuantumParticle(x=2, p=5.0)

print(p1)
print(p2)

print(p1.entangle(p2))
p1.spin()  # measure spin, other’s spin should flip
print(p1)
print(p2)

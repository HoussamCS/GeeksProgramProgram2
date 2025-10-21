import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self._radius = radius
        elif diameter is not None:
            self._radius = diameter / 2
        else:
            raise ValueError("You must provide either a radius or a diameter.")

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError("Diameter must be positive.")
        self._radius = value / 2

    @property
    def area(self):
        return math.pi * (self._radius ** 2)

    # 🟢 Dunder methods
    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __add__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Can only add Circle to Circle.")
        return Circle(radius=self.radius + other.radius)

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius


# ✅ Example usage
c1 = Circle(radius=4)
c2 = Circle(diameter=10)
c3 = Circle(radius=2)

print(c1)  # Circle(radius=4.00, diameter=8.00, area=50.27)
print(c2)  # Circle(radius=5.00, diameter=10.00, area=78.54)

# Addition
c3_new = c1 + c2
print(c3_new)  # Circle(radius=9.00, diameter=18.00, area=254.47)

# Comparisons
print(c1 == c2)  # False
print(c1 < c2)   # True
print(c1 > c3)   # True

# Sorting
circles = [c1, c2, c3, c3_new]
sorted_circles = sorted(circles)
for c in sorted_circles:
    print(c)

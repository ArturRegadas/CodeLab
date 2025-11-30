import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self):
        # pi * r²
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        # 2 * pi * r
        return 2 * math.pi * self.radius


circles = [
    Circle(1.5),
    Circle(3.0),
    Circle(4.75)
]

for c in circles:
    print(f"Radius: {c.radius}")
    print(f"Area: {c.calculate_area():.4f}")
    print(f"Perimeter: {c.calculate_perimeter():.4f}")
    print("-" * 30)

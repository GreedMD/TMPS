import copy

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.color = None

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) in {self.color} color"

    def clone(self):
        return copy.deepcopy(self)


if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2020)
    car1.color = "Red"
    print(car1)

    car2 = car1.clone()
    car2.color = "Blue"
    print(car2)

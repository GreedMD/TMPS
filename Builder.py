from abc import ABC, abstractmethod

class CarBuilder(ABC):
    @abstractmethod
    def build_engine(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_interior(self):
        pass

    @abstractmethod
    def get_car(self):
        pass

class Car:
    def __init__(self):
        self.engine = None
        self.body = None
        self.interior = None

    def __str__(self):
        return f"Car with {self.engine}, {self.body}, and {self.interior}."

class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def build_engine(self):
        self.car.engine = "V8"

    def build_body(self):
        self.car.body = "Sport"

    def build_interior(self):
        self.car.interior = "Leather"

    def get_car(self):
        return self.car

class SUVBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def build_engine(self):
        self.car.engine = "V6"

    def build_body(self):
        self.car.body = "SUV"

    def build_interior(self):
        self.car.interior = "Cloth"

    def get_car(self):
        return self.car

class Director:
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def construct_car(self):
        self.builder.build_engine()
        self.builder.build_body()
        self.builder.build_interior()

if __name__ == "__main__":
    # Build a sports car
    builder = SportsCarBuilder()
    director = Director(builder)
    director.construct_car()
    car = builder.get_car()
    print(car)

    # Build an SUV
    builder = SUVBuilder()
    director = Director(builder)
    director.construct_car()
    car = builder.get_car()
    print(car)

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Product class for cars
class Car:
    def __init__(self, brand: str, model: str, color: str):
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self) -> str:
        return f"{self.color} {self.brand} {self.model}"


# Object pool class for cars
class CarPool:
    def __init__(self, cars: List[Car]):
        self._cars = cars
        self._used_cars = set()

    def acquire_car(self) -> Car:
        if not self._cars:
            print("All cars are in use. Cannot create new car.")
            return None

        car = self._cars.pop()
        self._used_cars.add(car)
        return car

    def release_car(self, car: Car) -> None:
        if car in self._used_cars:
            self._used_cars.remove(car)
            self._cars.append(car)


# Creator abstract class for creating cars
class CarCreator(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass


# Concrete creators for creating specific types of cars
class HatchbackCreator(CarCreator):
    def __init__(self, car_pool: CarPool):
        self._car_pool = car_pool

    def create_car(self) -> Car:
        car = self._car_pool.acquire_car()
        if car:
            car.brand = "Honda"
            car.model = "Fit"
        return car


class SedanCreator(CarCreator):
    def __init__(self, car_pool: CarPool):
        self._car_pool = car_pool

    def create_car(self) -> Car:
        car = self._car_pool.acquire_car()
        if car:
            car.brand = "Toyota"
            car.model = "Camry"
        return car


class SUVCreator(CarCreator):
    def __init__(self, car_pool: CarPool):
        self._car_pool = car_pool

    def create_car(self) -> Car:
        car = self._car_pool.acquire_car()
        if car:
            car.brand = "Ford"
            car.model = "Explorer"
        return car


# Client code that uses the creators and object pool to create and release cars
if __name__ == "__main__":
    car_pool = CarPool([
        Car("Honda", "Fit", "Red"),
        Car("Toyota", "Camry", "Blue"),
        Car("Ford", "Explorer", "Green")
    ])

    creators = [HatchbackCreator(car_pool), SedanCreator(car_pool), SUVCreator(car_pool)]

    for i in range(7):
        print(f"Creating car {i+1}...")
        creator = creators[i % len(creators)]
        car = creator.create_car()
        if car:
            print(f"Created car: {car}")
            car_pool.release_car(car)
        print("")

    print(f"Cars in pool: {[str(car) for car in car_pool._cars]}")
    print(f"Cars in use: {[str(car) for car in car_pool._used_cars]}")

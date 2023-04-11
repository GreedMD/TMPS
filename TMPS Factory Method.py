from abc import ABC, abstractmethod


# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass


# Concrete products
class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

class Cow(Animal):
    def speak(self) -> str:
        return "Moo!"
class AnimalCreator(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass
class DogCreator(AnimalCreator):
    def create_animal(self) -> Animal:
        return Dog()
class CatCreator(AnimalCreator):
    def create_animal(self) -> Animal:
        return Cat()
class CowCreator(AnimalCreator):
    def create_animal(self) -> Animal:
        return Cow()
def client_code(creator: AnimalCreator):
    animal = creator.create_animal()
    print(f"The {type(animal).__name__} says: {animal.speak()}")
if __name__ == "__main__":
    print("Creating animals using different creators:")
    client_code(DogCreator())
    client_code(CatCreator())
    client_code(CowCreator())

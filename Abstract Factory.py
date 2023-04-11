from __future__ import annotations
from abc import ABC, abstractmethod

class CarFactory(ABC):
    @abstractmethod
    def create_sedan(self) -> Sedan:
        pass
    @abstractmethod
    def create_suv(self) -> SUV:
        pass
class Sedan(ABC):
    @abstractmethod
    def start(self) -> None:
        pass
class SUV(ABC):
    @abstractmethod
    def start(self) -> None:
        pass
class ToyotaFactory(CarFactory):
    def create_sedan(self) -> Corolla:
        return Corolla()
    def create_suv(self) -> RAV4:
        return RAV4()
class Corolla(Sedan):
    def start(self) -> None:
        print("Starting Corolla...")
class RAV4(SUV):
    def start(self) -> None:
        print("Starting RAV4...")
def client_code(factory: CarFactory) -> None:
    sedan = factory.create_sedan()
    suv = factory.create_suv()
    sedan.start()
    suv.start()
if __name__ == "__main__":
    print("Client: Testing code with ToyotaFactory.")
    toyota_factory = ToyotaFactory()
    client_code(toyota_factory)

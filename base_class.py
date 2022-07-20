from abc import ABC, abstractmethod


# Abstract classes:

class Service(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Engine(Service):
    pass


class Battery(Service):
    pass


# Concrete class:

class Car(Service):

    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery

    def needs_service(self) -> bool:
        return self._engine.needs_service() or self._battery.needs_service()
               
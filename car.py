from abc import ABC, abstractmethod
from battery.battery import Battery
from engine.engine import Engine


class Serviceable(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        self.engine.needs_service() or self.battery.needs_service()
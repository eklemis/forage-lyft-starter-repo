from abc import ABC, abstractmethod


class Tire(ABC):
    def __init__(self, tires_worn: list):
        # Check if the length of tires_worn is 4
        if len(tires_worn) != 4:
            raise ValueError("Expected a list of 4 tire wear values.")

        # Check if all values are between 0 and 1
        for tire in tires_worn:
            if not 0 <= tire <= 1:
                raise ValueError("Tire wear values should be between 0 and 1 inclusive.")

        self.tires_worn = tires_worn

    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Carrigan(Tire):
    def needs_service(self) -> bool:
        for tire_worn in self.tires_worn:
            if tire_worn >= 0.9:
                return True
        return False


class Octoprime(Tire):
    def needs_service(self) -> bool:
        return sum(self.tires_worn) >= 3


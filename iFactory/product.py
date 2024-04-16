from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Car(Vehicle):
    def __init__(self, model):
        self._model = model
    
    def deliver(self):
        return f"Car {self._model} delivered"

class Truck(Vehicle):
    def __init__(self, model):
        self._model = model

    def deliver(self):
        return f"Truck {self._model} delivered"

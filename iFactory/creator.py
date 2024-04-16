from abc import ABC, abstractmethod
fromproduc import Car, Truck

class VehicleFactory(ABC):
  @abstractmethod
  def get_vehicle(self, vehicle_type):
    pass

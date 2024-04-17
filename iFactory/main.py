from client_code import client_vehicle_code
from concrete_factory import CarFactory, TruckFactory

if __name__ == "__main__":
  client_vehcile_code(CarFactory(), vehicle_type:"SEDAN")
  client_vehcile_code(TruckFactory(), vehicle_type:"REMOLQUE")

# Clase del patron
class Singleton:
  _instances = {}

  def __new__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super().__new__(cls)

    return cls._instances[cls]

# Ejemplo para entender funcionamiento
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2) #Devuelve True

# Ejemplo de aplicacion para conexion a BD
import sqlite3

class DatabaseConnection(Singleton):
  connection = None

  def __init__(self):   # Metodo para conectar
    if self.connection is None:
      self.connection = sqlite3.connect("database_name")

  def execute_query(self, query):
    cursor = self.connection.cursor()
    cursor.execute(query)
    self.connection.commit()

  def close(self):
    self.connection.close()

# Prueba implementacion
db1 = DatabaseConnection()
db1.execute_query("CREATE TABLE IF NOT EXIST users (id INTEGER PRIMARY KEY, name TEXT")

# Segunda conexión para insertar
db2 = DatabaseConnection()
db2.execute_query("INSERT INTO users (name) VALUES ('my_user')")

print(db1 is db2) #Si funciona, tiene que dar True

# La conexion puede cerrarse tanto con db1 como db2
db1.close()

from fare import Fare
from ride import Ride

# Creamos la clase Taximetro en la que intanciaremos Tarifa y Carrera, y será en la que tendremos el menu de comandos del programa
class Taximeter:
    def __init__(self):
        # Instanciamos la clase Tarifa y le pasamos los parámetros de las tarifas establecidas
        self.fare = Fare(0.02, 0.05)
        # Instanciamos la clase Ride pasándole el parámetro Tarifa
        self.ride = Ride(self.fare)

    # Método para la Bienvenida y Menú de comandos
    def command_menu(self):
        pass
        



# Espacio para crear Instancia de nuevo Taximetro y llamada a métodos (menu...)
# Hola
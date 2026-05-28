from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def arrancar(self):
        pass
class auto(Vehiculo):
    def acelerar(self):
        print("El auto esta arrancando")
    def arrancar(self):
        print("El auto arranca")
    def detener(self):
        print("El auto se ha detendio")
class moto(Vehiculo):


Auto = auto()
Auto.acelerar()
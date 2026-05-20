
class Animal:
    def __init__ (self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie 

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Especie: {self.especie}")

    def hablar(self):
        print("hola !!")

    def moverse(self):
        print("estoy moviendome")

perro = Animal("dogi", 3, "perro" )
gato = Animal("michifu", 4, "gato")
pajaro = Animal("canigga", 56, "ave")


print(perro.nombre)             #atributos
print(perro.edad)
print(perro.especie)


perro.hablar()              #Metodos
gato.moverse()
pajaro.moverse()

#### Clase Persona -------------------------------------------------------

class Persona:
    def __init__(self, Nombre, apellido, DNI, Edad): #constructor
        self.nombre = Nombre
        self.apellido = apellido
        self.DNI = DNI
        self.Edad = Edad

    def hablar(self):
        print("A Roman lo tiene que matar")        

    def Presentarse(self):
        print(f"Hola, me llamo {self.nombre} {self.apellido}, mi Dni es {self.DNI}, y tengo {self.edad} años")

Benja = Persona("benja", "lopeztachi", 44491202, 20)

Benja.Presentarse

class Alumno(Persona):
    def __init__(self, nombre, edad, carrera, nota):
        super().__init__(nombre, edad)
        self.carrera = carrera 


messi = Persona("leonel", 38)

class Docente(Persona):
    def __init__(self, nombre, edad, Catedras, HoraCatedras):
        super().__init__(nombre, edad)
        self.catedras = Catedras
        self.horacatedras = HoraCatedras

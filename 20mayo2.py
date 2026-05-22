##es lo mismo que la anterior pero con objetos jeje
#Las clases tiene atributos y metodos
#en este caso atributos de la mascota (nombre, raza, edad, energia)
#Metodos = jugar , alimentar
class Mascota: 
    def __init__(self, nombre, especie, edad, energia = 20): # ]
        self.nombre = nombre #                              ]
        self.especie = especie #        Constructor               ]
        self.edad = edad #         Atributos                ]
        self.energia = energia #                         #  ]
    def alimentar(self, cantidad): #                        }
        self.energia += cantidad #         Metodo           }
    def jugar(self, tiempo): #                              }
        self.energia -= tiempo * 5 #                        }
    def saludar(self):
        return f'Mascota(nombre={self.nombre}, especie={self.especie}, edad={self.edad})'

class Perro(Mascota):
    def __init__(self, nombre, especie, raza, edad, energia=20): #copiamos todo y agregamos raza
        super().__init__(nombre, especie, edad, energia) #Super = Clsae Madre, llama a super
        self.raza = raza # agregamos raza
    def buscar_pelota(self):
        return f'{self.nombre} esta buscando la pelota...'
    def saludar(self):
        return f'Guau! Mi nombre es {self.nombre}, soy un {self.raza}'
class Ave(Mascota):
    def __init__(self, nombre, especie, color, raza, edad, energia=20):
        super().__init__(nombre, especie, edad, energia)
        self.color = color
        self.raza = raza
    def enviar_mensaje(self):
        if self._mensaje_vuelo is not None:
            print(f"  {self.nombre} ya está en vuelo con un mensaje. Esperá que vuelva.")
            return

        mensaje = input(f"  Escribí el mensaje para enviar con {self.nombre}: ")
        self._mensaje_vuelo = mensaje
        print(f"  {self.nombre} salió volando con tu mensaje... 🕊️")

    def recibir_mensaje(self):
        if self._mensaje_vuelo is None:
            print(f"  {self.nombre} no tiene ningún mensaje pendiente.")
            return

        print(f"  {self.nombre} llegó con el mensaje:")
        print(f"  >>> {self._mensaje_vuelo}")
        self._mensaje_vuelo = None   # el mensaje se entregó, paloma libre

dogui = Perro('dogui','Perro', 'labrador', 3)
pirulo = Perro('Pirulo','Perro', 'Beagle', 2)
paloma = Ave('pepe', 'paloma', 'gris', 'mensajera', 2, 3)

print(dogui)
print(pirulo)
print(dogui.saludar())
print(pirulo.saludar())

paloma.enviar_mensaje()
print()

input('presiona enter cuando quieras recibir el mensaje')
print()

paloma.recibir_mensaje()

#==========================================


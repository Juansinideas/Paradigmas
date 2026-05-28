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
    def enviar_mensaje(self, mensaje):
        print('pio pio, decime un mensaje que quieras enviar')
        input(mensaje)
        return f'pio pio pio, el mensaje es el siguiente: {mensaje}'

dogui = Perro('dogui','Perro', 'labrador', 3)
pirulo = Perro('Pirulo','Perro', 'Beagle', 2)
paloma = Ave('pepe', 'paloma', 'gris', 'mensajera', 2, 3)

print(dogui)
print(pirulo)
print(dogui.saludar())
print(pirulo.saludar())

paloma.enviar_mensaje() #ESTA MAL :( 
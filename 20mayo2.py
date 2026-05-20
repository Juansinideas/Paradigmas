##es lo mismo que la anterior pero con objetos jeje
#Las clases tiene atributos y metodos
#en este caso atributos de la mascota (nombre, raza, edad, energia)
#Metodos = jugar , alimentar
class Mascota: 
    def __init__(self, nombre, raza, edad, energia = 20): # ]
        self.nombre = nombre #                              ]
        self.raza = raza #        Constructor               ]
        self.edad = edad #         Atributos                ]
        self.energia = energia #                         #  ]
    def alimentar(self, cantidad): #                        }
        self.energia += cantidad #         Metodo           }
    def jugar(self, tiempo): #                              }
        self.energia -= tiempo * 5 #                        }
    def __str__(self):
        return f'Mascota(nombre={self.nombre}, raza={self.raza}, edad={self.edad})'


dogui = Mascota('dogui', 'labrador', 3)
pirulo = Mascota('Pirulo', 'Beagle', 2, 40)

print(dogui)
print(pirulo)
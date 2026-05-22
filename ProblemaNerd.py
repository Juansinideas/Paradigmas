#Ejercicio Characters:
#Se quiere desarrollar un sistema simple para representar personajes de un juego de rol. 
# Cada personaje tiene un nombre, una clase de personaje (guerrero, mago, arquero, etc.), un nivel, puntos de vida (HP) 
# y puntos de maná (MP).

#Los personajes pueden atacar, recibir daño, usar habilidades especiales y mostrar su 
# información en pantalla. Diferentes tipos de personajes tienen comportamientos distintos:
#  un guerrero ataca cuerpo a cuerpo con fuerza bruta; un mago lanza hechizos a distancia gastando 
# maná; un arquero dispara flechas con alta precisión.

class Champ:
    def __init__(self, nombre:str, clase:str, nivel=1, hp=100):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.hp = hp 
    def __str__(self):
        return f'{self.nombre} es un {self.clase} de nivel {self.nivel} con {self.hp} puntos de vida'
    def DañoRecibido(self, daño):
        self.hp -= daño
        print(f'{self.nombre} recibio {daño} de daño. le quedan {self.hp} de vida' )
class Bruiser(Champ):
    def __init__(self, nombre, clase, daño, nivel, hp):
        super().__init__(nombre, clase, nivel, hp)
        self.daño = daño
    def GolpeMelee(self, enemigo):
        print(f'{self.nombre} ataca con mucha fuerza a {enemigo.nombre}')
        daño_causado =  self.daño
        enemigo.DañoRecibido(daño_causado)
garen = Bruiser('Garen', 'Brusier', 3, 1, 100)
darius = Bruiser('Darius', 'Brusier', 3, 1, 100)
print(garen)
garen.GolpeMelee(darius)

class Tirador(Champ):
    def __init__(self, nombre, clase, rango, nivel, hp):
        super().__init__(nombre, clase, nivel, hp)
        self.rango = rango 
    def GolpeRanged(self, enemigo):
        print(f'{self.nombre} ha disparado a {enemigo.nombre} desde {self.rango}m')
        daño_causado = self.rango / 2 
        enemigo.DañoRecibido(daño_causado)

draven = Tirador('Draven', 'Tirador', 50, 2, 50)

draven.GolpeRanged(garen)
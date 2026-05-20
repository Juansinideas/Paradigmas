def crear_mascota(nombre, raza, edad, energia=50):
    return {
        "nombre" : nombre,
        "raza" : raza,
        "edad" : edad,
        "energia" : energia
    }
def alimentar_mascota(mascota, cantidad):
    mascota['energia'] += cantidad

def jugar(mascota, tiempo):
    mascota['energia'] -= tiempo * 5 


dogui=crear_mascota("pelusa","Labrador", 4)
pirulo=crear_mascota("pirulo","caniche",3, 70)
print(dogui)
print(pirulo)

alimentar_mascota(dogui, 20)
alimentar_mascota(pirulo, 39)

print(dogui)
print(pirulo)

jugar(dogui, 100)
jugar(pirulo, 3)

print(dogui)
print(pirulo)
def crear_mascota(nombre, raza, edad, energia=50):
    return {
        "nombre" : nombre,
        "raza" : raza,
        "edad" : edad,
        "energia" : energia
    }
def alimentar_mascota(mascota, cantidad):
    mascota['energia'] += cantidad


dogui=crear_mascota("pelusa","Labrador", 4)
pirulo=crear_mascota("pirulo","caniche",3, 70)
print(dogui)
print(pirulo)


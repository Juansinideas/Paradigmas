def crear_mascota(nombre, raza, edad, energia=50)
    return {
        "nombre" : nombre,
        "raza" : raza,
        "edad" : edad,
        "energia" : energia
    }
dogui=crear_mascota("pelusa","Labrador", 4)
pirulo=crear_mascota("pirulo","caniche",3)
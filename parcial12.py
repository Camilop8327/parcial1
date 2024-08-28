class Mascota:

    def __init__(self,nombre,especie):

        self.nombre=nombre
        self.especie=especie

gato=Mascota("Mono", "Gato")
perro=Mascota("Lucas", "Perro")

print(type(gato))
print(type(perro))

print(gato.nombre, gato.especie)
print(perro.nombre, perro.especie)
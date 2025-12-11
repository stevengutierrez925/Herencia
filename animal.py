class animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_detalles(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")

class perro(animal):
    def emitir_sonido(self):
        print("guau guau")

class gato(animal):
    def emitir_sonido(self):
        print("miau miau")

if __name__ == "__main__":
    p = perro("firulais", 3)
    p.mostrar_detalles()
    p.emitir_sonido()
    print()

    g = gato("chambi", 2)
    g.mostrar_detalles()
    g.emitir_sonido()

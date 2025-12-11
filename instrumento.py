class instrumento:
    def __init__(self, nombre, material):
        self.nombre = nombre
        self.material = material
    
    def tipo_sonido(self):
        print("este instrumento produce sonido musical")

    def mostrar_detalles(self):
        print(f"nombre: {self.nombre}")
        print(f"material: {self.material}")

class guitarra(instrumento):
    def tocar_nota(self):
        print("sonido: strummm")

class piano(instrumento):
    def tocar_nota(self):
        print("sonido: plinnn")

if __name__ == "__main__":
    g = guitarra("guitarra acustica", "madera")
    g.mostrar_detalles()
    g.tocar_nota()

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_info(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")

class estudiante(persona):
    def asignar_rol(self):
        return "soy estudiante"

    def mostrar_info_especifica(self):
        print(f"{self.nombre} es estudiante y tiene {self.edad} anios")

class profesor(persona):
    def asignar_rol(self):
        return "soy profesor"

    def mostrar_info_especifica(self):
        print(f"{self.nombre} es profesor y tiene {self.edad} anios")

if __name__ == "__main__":
    e = estudiante("steven", 17)
    e.mostrar_info()
    print(e.asignar_rol())

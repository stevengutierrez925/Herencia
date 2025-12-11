class empleado:
    def __init__(self, nombre, salario, cargo):
        self.nombre = nombre
        self.salario = salario
        self.cargo = cargo
    
    def mostrar_detalles(self):
        print(f"nombre: {self.nombre}")
        print(f"salario: {self.salario}")
        print(f"cargo: {self.cargo}")

class gerente(empleado):
    def calcular_aumento(self):
        aumento = self.salario * 0.15  # 15% de aumento
        return self.salario + aumento

class empleado_temporal(empleado):
    def calcular_aumento(self):
        aumento = self.salario * 0.05  # 5% de aumento
        return self.salario + aumento

if __name__ == "__main__":
    g = gerente("juan", 50000, "gerente")
    g.mostrar_detalles()
    print(f"salario con aumento: {g.calcular_aumento()}")
    print()

    e = empleado_temporal("maria", 20000, "temporal")
    e.mostrar_detalles()
    print(f"salario con aumento: {e.calcular_aumento()}")

class vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def mostrar_detalles(self):
        print(f"marca: {self.marca}")
        print(f"modelo: {self.modelo}")
        print(f"anio: {self.anio}")

class automovil(vehiculo):
    def eficiencia_combustible(self, km, litros):
        return km / litros

    def combustible_necesario(self, distancia, km_por_litro):
        return distancia / km_por_litro

class motocicleta(vehiculo):
    def eficiencia_combustible(self, km, litros):
        return km / litros

    def combustible_necesario(self, distancia, km_por_litro):
        return distancia / km_por_litro

if __name__ == "__main__":
    a = automovil("ford", "focus", 2020)
    a.mostrar_detalles()
    print(f"eficiencia: {a.eficiencia_combustible(500, 50)} km/l")
    print(f"combustible para 300 km: {a.combustible_necesario(300, 10)} litros")

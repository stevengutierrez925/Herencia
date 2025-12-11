class transporte:
    def __init__(self, capacidad, velocidad_maxima):
        self.capacidad = capacidad
        self.velocidad_maxima = velocidad_maxima
    
    def mostrar_detalles(self):
        print(f"capacidad: {self.capacidad}")
        print(f"velocidad maxima: {self.velocidad_maxima} km/h")

class avion(transporte):
    def tiempo_viaje(self, distancia):
        return distancia / self.velocidad_maxima

class barco(transporte):
    def tiempo_viaje(self, distancia):
        return distancia / self.velocidad_maxima

if __name__ == "__main__":
    a = avion(180, 900)
    a.mostrar_detalles()
    print("tiempo de viaje:", a.tiempo_viaje(1800), "horas")

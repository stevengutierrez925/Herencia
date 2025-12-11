from datetime import date

class producto:
    def __init__(self, nombre, precio, fecha_vencimiento):
        self.nombre = nombre
        self.precio = precio
        self.fecha_vencimiento = fecha_vencimiento
    
    def mostrar_detalles(self):
        print(f"nombre: {self.nombre}")
        print(f"precio: {self.precio}")
        print(f"fecha de vencimiento: {self.fecha_vencimiento}")

class producto_alimenticio(producto):
    def aplicar_descuento(self):
        hoy = date.today()
        dias = (self.fecha_vencimiento - hoy).days
        
        if dias <= 5:
            return self.precio * 0.7   # 30% descuento
        return self.precio

class producto_electronico(producto):
    def aplicar_descuento(self):
        # descuento si vale mas de 100000
        if self.precio > 100000:
            return self.precio * 0.85  # 15%
        return self.precio

if __name__ == "__main__":
    p1 = producto_alimenticio("leche", 1200, date(2025, 11, 25))
    p1.mostrar_detalles()
    print("precio con descuento:", p1.aplicar_descuento())

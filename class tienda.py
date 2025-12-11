class tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []
        self.ventas = 0
    
    def mostrar_info(self):
        print(f"tienda: {self.nombre}")
        print(f"productos en inventario: {len(self.inventario)}")
        print(f"total de ventas: {self.ventas}")

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.inventario:
            self.inventario.remove(producto)

class tienda_ropa(tienda):
    def vender(self, precio):
        self.ventas += precio

class tienda_electronica(tienda):
    def vender(self, precio):
        self.ventas += precio

if __name__ == "__main__":
    t = tienda_ropa("ropa steven")
    t.agregar_producto("remera")
    t.vender(5000)
    t.mostrar_info()

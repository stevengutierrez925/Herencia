class pago:
    def __init__(self, monto, fecha):
        self.monto = monto
        self.fecha = fecha
    
    def mostrar_detalles(self):
        print(f"monto: {self.monto}")
        print(f"fecha: {self.fecha}")

class pago_tarjeta(pago):
    def procesar(self):
        print("procesando pago con tarjeta... aprobado")

    def recibo(self):
        print(f"recibo tarjeta por ${self.monto}")

class pago_paypal(pago):
    def procesar(self):
        print("procesando pago con paypal... aprobado")

    def recibo(self):
        print(f"recibo paypal por ${self.monto}")

if __name__ == "__main__":
    p = pago_tarjeta(15000, "2025-11-20")
    p.mostrar_detalles()
    p.procesar()
    p.recibo()

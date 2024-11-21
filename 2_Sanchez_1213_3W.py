print(" ")
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ")

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        if not titular:
            raise ValueError("El titular es obligatorio.")
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad

cuenta = Cuenta("Ana")
cuenta.mostrar()

cuenta.ingresar(300)
cuenta.mostrar()

cuenta.retirar(100)
cuenta.mostrar()

cuenta.retirar(500) 
cuenta.mostrar()

print(" ")
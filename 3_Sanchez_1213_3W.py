print(" ")
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ")

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}")

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def esTitularValido(self):
        return 18 <= self.cantidad < 25

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero: el titular no es válido.")

    def mostrar(self):
        print(f"Cuenta Joven - Titular: {self.titular}, Cantidad: {self.cantidad:.2f}, Bonificación: {self.bonificacion}%")

cuenta_joven = CuentaJoven("Ana", cantidad=20, bonificacion=10)
cuenta_joven.mostrar()

cuenta_joven.ingresar(100)
cuenta_joven.mostrar()

cuenta_joven.retirar(50)
cuenta_joven.mostrar()

cuenta_joven.cantidad = 30  
cuenta_joven.retirar(50)

print(" ")
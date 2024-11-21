print(" ")
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ")

class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    def esMayorDeEdad(self):
        return self.edad >= 18

persona = Persona("Ana", 30, "12345678A")
persona.mostrar()
print("Es mayor de edad:", persona.esMayorDeEdad())

print(" ")
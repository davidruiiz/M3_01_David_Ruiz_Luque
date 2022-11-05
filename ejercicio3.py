'''
Ejercicio 3
Creación
Crea una clase llamada Producto que tenga los atributos codigo, nombre, precio y tipo.
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el producto se ha creado con éxito
Crea el método __str__ para visualizar por pantalla la información de los productos
Experimentación
Crea algunos productos
Prueba a mostrar los datos de algun producto y a modificar algun valor, por ejemplo, prueba a modificar el precio de un producto
'''
#Creación
class Alumno():

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print('\nEl alumno se ha creado con éxito.')

    def __str__(self):
        return '\nEl alumno {} ha sacado un {}.'.format(self.nombre, self.nota)

    def calificacion(self):
        if self.nota >= 5:
            return print('\n{} ha aprobado con un {}.'.format(self.nombre, self.nota))
        else:
            return print('\n{} ha suspendido con un {}.'.format(self.nombre, self.nota))

class Producto():
   
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print('El constructor se ha creado con éxito.')
#Experimentación

alumno1=Alumno('David', 8)
alumno2=Alumno('Victor', 4)
print(alumno1)
print(alumno2)
Alumno.calificacion(alumno1)
Alumno.calificacion(alumno2)

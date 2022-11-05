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

class Producto():
   
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print('\nEl producto se ha creado con éxito.')

    def __str__(self):
        return 'El producto con código {} y nombre "{}" tiene un precio de {} y es del tipo {}.\n'.format(self.codigo,  self.nombre, self.precio, self.tipo)

#Experimentación

producto1=Producto('NH87616', 'Cepillo de dientes', '3€', 'manual')
print(producto1)
producto2=Producto('VB001-2', 'ordenador', '600€', 'portátil')
print(producto2)

self.precio[producto2]='200'
print(producto2)
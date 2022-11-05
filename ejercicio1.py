"""
Ejercicio 1
Creación
Crea una clase llamada Alumno que tenga los atributos nombre y nota
Crea el constructor de la clase. Añadir en el constructor un print 
para informar de que el alumno se ha creado con éxito
Crear un método llamado calificacion que imprima por pantalla 
si el alumno ha aprobado o suspendido en base a su nota
Experimentación
Crea algunos alumnos
Prueba a ejecutar el método calificacion de cada objeto que has creado
"""

#Creación
class Alumno():

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print('\nEl alumno se ha creado con éxito.')

    def calificacion(self):
        if self.nota >= 5:
            return print('\n{} ha aprobado con un {}'.format(self.nombre, self.nota))
        else:
            return print('\n{} ha suspendido con un {}'.format(self.nombre, self.nota))

#Experimentación
alumno1=Alumno('David', 8)
Alumno.calificacion(alumno1)
alumno2=Alumno('Victor', 4)
Alumno.calificacion(alumno2)
        

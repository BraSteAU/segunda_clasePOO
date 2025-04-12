#Estructura basica de una clase
#definimos una clase con la palabra clave class y el constructor es el metodo especial
# __init__. Este metodo se ejecuta al crear una instancia, siempre se acompaña con el parametro
# self y este self hace referencia al objeto creado.

#Atributos de clase y de instancia:
#   -Atributos de instancia son atributos que se inicializan en el constructor de la clase objeto mantiene sus propios valores
#
#   -Atributos de clase por el contrario se definen directamente en la clase y son compartidos por todas las instancias

#Encapsulamiento: consiste en ocultar la implementacion interna ( por ejemplo, declarando atributos como privados con dos guiones bajos)
#   y exponer metodos publicos para interactuar con ellos.

#Herencia: permite que una clase derive de otra, heredando sus atributos y metodos, lo cual favorece la reutilizacion y extension del codigo.

#Polimorfismo: mediante la sobreescritura de metodos, diferentes cclases pueden implementar comportamientos especificos apesar de compartir
#   la misma interfaz o metodo de la clase base.


class Persona:
    #constructor con atributos de instancia
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def presentarse(self):
        print("Hola, mi nombre es ",self.nombre," y tengo ",self.edad," años")
    
#Creacion de instancias
persona1=Persona("Isabela",23)
persona2=Persona("Brayan",27)

#Uso del metodo para mostrar la informacion de cada instancia
persona1.presentarse()
persona2.presentarse()
class Vehiculo:
    #atributo de clase que se compartira entre todas las instancias
    tipo="Transporte"
    def __init__(self,marca,modelo,year):
        self.marca=marca
        self.modelo=modelo
        self.year=year
    
    def informacion(self):
        print("Vehiculo ",self.marca,self.modelo," del año ",self.year)
        print("Tipo",Vehiculo.tipo)

vehiculo1=Vehiculo("BMW","M4",2023)
vehiculo2=Vehiculo("Mazda","3",2021)

vehiculo1.informacion()
vehiculo2.informacion()
        
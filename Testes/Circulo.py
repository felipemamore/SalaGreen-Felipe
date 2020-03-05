import math
class Circulo:
    def __init__(self, cor, raio, material):
        self.cor = cor
        self.__raio = raio
        self.__material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        return self.cor
    def area(self):
        #self.__raio = raio
        return self.__raio*(math.pi**2)





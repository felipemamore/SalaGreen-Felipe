import math
class Circulo:
    def __init__(self, cor, material, raio):
        self.cor = cor
        self.raio = raio
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor
    def mostraCor(self):
        return self.cor
    def area(self, raio):
        self.raio = raio
        return self.raio*(math.pi**2)
    def setMaterial(self,material):
        self.__material=material
        pass
    def getMaterial(self,material):
        return self.material





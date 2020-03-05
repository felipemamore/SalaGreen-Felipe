class Quadrado:
    def __init__(self, lado):
        self.__lado = lado

    def setLado(self, lado):
        self.__lado = lado

    def getLado(self):
        return self.__lado

    def calc_area(self):
        self.__area = self.__lado * self.__lado
        return self.__area

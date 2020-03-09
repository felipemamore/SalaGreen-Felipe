class Endereco:
    def __init__(self) -> None:
        self.__rua = ''
        self.__bairro = ''
        self.__cidade = ''

    def getRua(self)-> str:
        return self.__rua

    def getBairro(self)-> str:
        return self.__bairro

    def getCidade(self)-> str:
        return self.__cidade

    def setRua(self, rua) -> None:
        if type(rua) == str:
            self.rua = rua


    def setBairro(self, bairro) -> None:
        if type(bairro) == str:
            self.__bairro = bairro


    def setCidade(self, cidade) -> None:
        if type(cidade) == str:
            self.__cidade == cidade



class Pessoa:
    def __init__(self, nome, idade, ocupacao, rua, bairro, numero, cidade):

        self.__nome = nome
        self.__idade = idade
        self.__ocupacao = ocupacao
        self.endereco=Endereco(rua, bairro, numero, cidade)


    def setNome(self, nome):
        self.__nome = nome
    def setIdade(self,idade):
        self.__idade = idade
    def setOcupacao(self,ocupacao):
        self.__ocupacao = ocupacao
    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def getOcupacao(self):
        return self.ocupacao

class Endereco:
    def __init__(self, rua, bairro, numero, cidade):
        self.__rua = rua
        self.__bairro = bairro
        self.__numero = numero
        self.__cidade = cidade
    def setRua(self, rua):
        self.__rua = rua
    def setBairro(self, bairro):
        self.__bairro = bairro
    def setNumero(self, numero):
        self.__numero = numero
    def setCidade(self, cidade):
        self.__cidade = cidade
    def getRua(self):
        return self.rua
    def getBairro(self):
        self.bairro
    def getNumero(self):
        return self.numero
    def getCidade(self):
        return self.cidade

class Engenheiro(Pessoa):
    def __init__(self, nome, idade, ocupacao, categoria, registro):
        super().__init__(nome, idade, ocupacao)
        self.__categoria=categoria
        self.__registro=registro
    def setCategoria(self, categoria):
        self.__categoria = categoria
    def setRegistro(self,registro):
        self.__registro=registro
    def getCategoria(self):
        return self.categoria
    def getRegistro(self):
        return self.registro
e=Engenheiro()
e.setCategoria()











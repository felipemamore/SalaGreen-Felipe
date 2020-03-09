from Classes.Endereco_Classe import Endereco
class Pessoa:
    def __init__(self,nome:str, sobrenome:str, idade:int) -> None:
        self.__nome = ''
        self.__sobrenome = ''
        self.__idade = 0
        # Atributo da classe Pessoa usando composiçao atraves do uso da classe endereco
        self.__endereco = Endereco()

        if type(nome) == str:
            self.__nome = nome
        if type (sobrenome) == str:
            self.__sobrenome = sobrenome
        if self.__verifica_idade(idade):
            self.__idade = idade

    def __verifica_idade(self, idade) -> bool:
        if type(idade) == int and idade > 0:
            return True
        return False


    def getNome(self) -> str:
        return self.__nome

    def getSobrenome(self) -> str:
        return self.__sobrenome

    def getIdade(self) -> int:
        return self.__idade

    def setNome(self, nome: str) -> None:
        if type(nome) == str:
            self.__nome = nome

    def setSobrenome(self,sobrenome:str) -> None:
        if type(sobrenome) == str:
            self.__sobrenome = sobrenome

    def set_idade(self, idade:int) -> None:
        if type(idade) == int and idade > 0:
            self.__idade = idade

    def get_endereco(self)-> Endereco:
        return self.__endereco

    def set_endereco(self, endereco: Endereco) -> None:
        self.__endereco = endereco



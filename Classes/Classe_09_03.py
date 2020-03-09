#Herança

from Classes.Pessoa_Classe import Pessoa
from Classes.Endereco_Classe import Endereco
class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, idade, registro, cargo):
        self.__numero_registro = registro
        self.__cargo = cargo
        super().__init__(nome, sobrenome, idade)

    def get_registro(self) -> int:
        return self.__numero_registro

    def get_cargo(self) -> str:
        return self.__cargo

    def set_registro(self, numero_registro)->None:
        self.__numero_registro = numero_registro

    def set_cargo(self, cargo) -> None:
        self.__cargo = cargo




p = Pessoa()






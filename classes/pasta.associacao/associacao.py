"""
Associação é quando duas classes estão relacionadas mas nenhuma das duas se dependem

"""


class Escritor:

    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    # Getter para transformar o atributo privado em livre para utilizar fora da classe
    @property
    def nome(self):
        return self.__nome

    # Getter e Setter para realizar a atribuição de uma ferramenta para o escritor
    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:

    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print("Caneta está escrevendo...")


class MaquinaDeEscrever:

    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    def escrever(self):
        print("Maquina de escrever está escrevendo...")

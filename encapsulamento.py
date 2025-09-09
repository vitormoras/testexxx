"""
encapsulamento podemos utilizar _ ou __ para proteger os dados
_protected (variavel pode ser alterada forçando a utilização de _)
__private (variavel é inalterada mesmo utilizando os dois __, ao invés disso se cria outra variavel para setar o valor depositado posteriomente)
salvo a situação de utilização _NOMECLASSE__nomeatributo
"""


class BancoDeDados:

    def __init__(self):
        self.__dados = {}

    def inserir_clientes(self, id, nome):
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id: nome}
        else:
            self.__dados["clientes"].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados["clientes"].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados["clientes"][id]


bd = BancoDeDados()

bd.inserir_clientes(1, "Vitor")
bd.inserir_clientes(2, "Hugo")
bd.inserir_clientes(3, "Moras")
bd.lista_clientes()
bd.apaga_cliente(3)
bd.__dados = "Outra coisa"
print(bd.__dados)
print("---------")
bd.lista_clientes()

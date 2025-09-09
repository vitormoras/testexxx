# Relação mais forte entre as classes, uma classe é dona de objetos de outra classe, ou seja caso a classe principal seja apagada,
# as outras classes vão perder esses objetos tbm


class Cliente:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = (
            []
        )  # Endereço vai receber outra classe, com uma lista vazia para implementar um cliente que pode ter varios endereços.

    def insere_endereço(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:

    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__


class Cliente(Pessoa):
    def comprando(self):
        print(f"{self.nome} está comprando...")


class Aluno(Pessoa):
    def estudando(self):
        print(f"{self.nome} está estudando...")

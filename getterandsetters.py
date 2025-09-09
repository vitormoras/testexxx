class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, desconto):
        self.preco -= self.preco * (desconto / 100)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # Getter -> vai obter o valor de algum atributo instanciado da classe
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))
        self._preco = valor


prod1 = Produto("camisa", 55)
prod1.desconto(12)

print(prod1.nome, prod1.preco)


prod2 = Produto("Caneca", "R$30")
prod2.desconto(10)

print(prod2.nome, prod2.preco)

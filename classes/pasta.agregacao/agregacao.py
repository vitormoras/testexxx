class CarrinhoDeCompra:

    def __init__(self):
        self.produtos = []

    def adicionar_produtos(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        sum_total = 0
        for produto in self.produtos:
            sum_total += produto.valor
        return sum_total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

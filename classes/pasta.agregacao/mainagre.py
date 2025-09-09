from agregacao import CarrinhoDeCompra, Produto

carrinho = CarrinhoDeCompra()


p1 = Produto("Camisinha", 55)
p2 = Produto("Camisinhona", 122)
p3 = Produto("Camisetoninha", 5512)

carrinho.adicionar_produtos(p1)
carrinho.adicionar_produtos(p2)
carrinho.adicionar_produtos(p3)

carrinho.listar_produtos()
print(carrinho.soma_total())

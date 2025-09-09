from composicao import Cliente, Endereco

cliente1 = Cliente("Vitor", 28)
cliente2 = Cliente("Mariazinha", 22)
cliente3 = Cliente("Bel", 28)

cliente1.insere_endereço("São Miguel", "PR")
cliente2.insere_endereço("Medianeira", "PR")
cliente3.insere_endereço("Medianeira", "PR")

print("-----------")
print(cliente1.nome)
cliente1.listar_endereco()
print("-----------")
print(cliente2.nome)
cliente2.listar_endereco()
print("-----------")
print(cliente3.nome)
cliente3.listar_endereco()

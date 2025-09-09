from associacao import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor("Joãozinho")
caneta = Caneta("BIC")
mq_escrever = MaquinaDeEscrever(1982)

print(f"Escritor {escritor.nome}")
print(f"A caneta da marca {caneta.marca}")
print(f"A máquina de escrever de {mq_escrever.age}")


"""
Associação entre escritor e a ferramenta para utilizar os métodos das outras classes como caneta e máquina
"""

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

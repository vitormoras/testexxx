from datetime import datetime
from random import randint


class Pessoa:

    ano_atual = int(datetime.strftime(datetime.now(), "%Y"))

    def __init__(self, nome, idade, comendo=False, falando=False, correndo=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.correndo = correndo

    # classmethod é um método de classe, podendo utilizar as variasveis da classe, ao invés de self se utiliza cls.
    @classmethod
    def ano_nascimento(cls, nome, idade):
        print(f"{nome} nasceu em {cls.ano_atual - idade}")
        return

    # staticmethod é um função que não utilizamos os as instancias (self) ou os métodos de classe (cls), mas podendo ser acessado pela instancia
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

    # métodos de instancia, precisa receber o (self)
    def comer(self, alimento):
        if self.falando == True:
            print(f"{self.nome} não pode comer falando.")
            return

        if self.correndo == True:
            print(f"{self.nome} não pode comer enquanto corre!")
            return

        print(f"{self.nome} está comendo {alimento}.")
        self.comendo = True

    def para_comer(self):
        if self.comendo == True:
            self.comendo = False
            return

        print(f"{self.nome} não está comendo")

    def falar(self, assunto):
        if self.comendo == True:
            print(f"{self.nome} não pode falar comendo")
            return

        if self.correndo == True:
            print(f"{self.nome} não pode falar correndo")
            return

        print(f"{self.nome} está falando sobre {assunto}")
        self.falando = True

    def para_falar(self):
        if self.falando == True:
            self.falando = False
            print(f"{self.nome} parou de falar.")
            return

        print(f"Não está falando")

    def correr(self):
        if self.comendo == True or self.falando == True:
            print(f"{self.nome} não pode correr")
            return

        print(f"{self.nome} está correndo!")
        self.correndo = True

    def parar_correr(self):
        if not self.correndo:
            print(f"Não está correndo")
            return

        print(f"{self.nome} parou de correr")
        self.correndo = False

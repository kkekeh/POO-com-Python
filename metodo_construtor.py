# O Método Construtor (inicializador), é chamado assim que a classe for instanciada.


class Pessoa:
    def __init__(self, nome):  # Método especial.
        self.nome = nome

    def mostra_dados(self):
        print(f'Meu nome é {self.nome}.')


p1 = Pessoa('Fulano')
p1.mostra_dados()

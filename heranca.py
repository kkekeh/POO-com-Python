# A Herança determina que uma classe (filha) herde atributos e métodos de uma outra classe (pai).


class Pessoa: # Pai.
    def __init__(self, nome):
        self.nome = nome
        self.nome_classe = self.__class__.__name__

    def falar(self):
        print(f'{self.nome_classe} está falando...')


class Professor(Pessoa):  # Filha (herda de Pessoa).
    
    def ensinar(self):
        print(f'{self.nome_classe} está ensinando...')


professor = Professor('Fulano')
professor.falar()  # Chamando o método herdado do Pai.
professor.ensinar()

from datetime import date

# O Método de Classe recebe como primeiro parâmetro o 'cls', que refere-se apenas à classe em si.


class Pessoa:
    ano_atual = date.today().year  # Retorna o ano atual da máquina.

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod  # Decorador que converte em um método de classe.
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        
        return cls(nome, idade)

    def mostra_dados(self):
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos.')


# OBJETOS
p1 = Pessoa('Fulano', 28)
p2 = Pessoa.por_ano_nascimento('Fulano', 1994)

# Note que o resultado é o mesmo.
p1.mostra_dados()
p2.mostra_dados()

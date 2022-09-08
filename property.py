# Mais segurança ao seu código.


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    # getter (acessa o atributo)
    @property  # Decorador que transforma atributos de classe em propriedades.
    def preco(self):
        return self._preco
    
    # setter (modifica o atributo)
    @preco.setter
    def preco(self, valor):
        
        if valor > 0:
            self._preco = valor
        else:
            print('O valor não pode ser negativo!')

    def mostra_dados(self):
        print(f'O {self.nome} custa R${self.preco:.2f}')


prod = Produto('Açaí', 16)
prod.mostra_dados()

# Note que o atributo não pôde ser alterado aqui.
prod.preco = -16

prod.preco = 18
prod.mostra_dados()

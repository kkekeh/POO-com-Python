# A classe (objeto-todo) se relaciona com outra classe (objeto-parte). Porém, o 'todo' é responsável por criar e destruir as suas 'partes'.


class Cliente():
    def __init__(self, nome):
        self.nome = nome
        self.endereco = []  # Array de objetos.
    
    def inserir_endereco(self, cidade, estado):
        self.endereco.append(Endereco(cidade, estado))
    
    def mostrar_dados(self):
        print(self.nome)

        for endereco in self.endereco:
            print(f'{endereco.cidade}-{endereco.estado}')
    
    def __del__(self):
        print(f'{self.nome} (objeto-todo) apagado!')


class Endereco():
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}-{self.estado} (objeto-parte) apagado!')


cliente = Cliente('Fulano')
cliente.inserir_endereco('Cidade', 'ESTADO')
cliente.mostrar_dados()

print('=' * 33)

# Note que, ao deletar o cliente, o endereço também será deletado.
del cliente

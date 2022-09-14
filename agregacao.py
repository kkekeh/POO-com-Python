# A classe (objeto-todo) se relaciona com outra classe (objeto-parte), mas nenhuma depende uma da outra.


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    
    def info(self):
        print(f'{self.nome} R${self.valor:.2f}')


class Carrinho:
    def __init__(self):
        self.produtos = []  # Array de objetos.

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def mostra_produtos(self):
        
        for produto in self.produtos:
            produto.info()


# OBJETOS
carrinho = Carrinho()
camisa = Produto('Camisa', 30)
shorts = Produto('Shorts', 40)

carrinho.inserir_produto(camisa)
carrinho.inserir_produto(shorts)
carrinho.mostra_produtos()

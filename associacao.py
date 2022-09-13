# A classe se relaciona com outra classe, mas nenhuma depende uma da outra.


class Escritor:
    def __init__(self):
        self.ferramenta = None


class Caneta:
    def __init__(self, marca):
        self.marca = marca

    def escrever(self):
        print(f'Escrevendo com a caneta {self.marca}...')


# OBJETOS
escritor = Escritor()
caneta = Caneta('Bic')

# Note que temos um objeto como atributo de outro objeto.
escritor.ferramenta = caneta
escritor.ferramenta.escrever()

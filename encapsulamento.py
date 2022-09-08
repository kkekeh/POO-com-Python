"""
public
_protected
__private (obj._Classe__nome)

nota 1: Não existem modificadores de acesso em Python, são apenas convenções (somos todos adultos responsáveis).

nota 2: Os atributos ou métodos ainda podem ser acessados/modificados. O que muda, é que o Python não deixa ser reatribuido valor para um atributo privado, ele cria outro com o mesmo nome na instância.
"""


class Dados:
    __privado = []

    def inserir_dado(self, dado):
        self.__privado.append(dado)


dados = Dados()
dados.inserir_dado('Qualquer coisa')
dados.inserir_dado('Outra coisa')
dados.__privado = 'test'

# Note que o atributo original não foi alterado.
print(dados.__privado)
print(dados._Dados__privado)

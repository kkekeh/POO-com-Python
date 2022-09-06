# Os Atributos de Classe são definidos dentro da própria classe.


class Pessoa:
    nome = 'Fulano'  # Atributo.


# OBJETOS
p1 = Pessoa()
p2 = Pessoa()

p2.nome = 'Fulana'

# Note que apenas o nome de p2 foi modificado.

print(Pessoa.nome)
print(p1.nome)
print(p2.nome)

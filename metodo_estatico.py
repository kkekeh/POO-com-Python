from random import randint

# O Método Estático não faz referência à classe (pode até ser criado fora do escopo) ou instância.


class Pessoa:

    @staticmethod  # Decorador que converte em um método estático. 
    def gera_id():
        return randint(0, 10)


p1 = Pessoa()
print(p1.gera_id())

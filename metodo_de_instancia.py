# O Método de Instância recebe como primeiro parâmetro o 'self', referindo-se à instância.


class Pessoa:
    
    def comer(self, alimento):
        print(f'Comendo {alimento}...')


pessoa = Pessoa()
pessoa.comer('açaí')

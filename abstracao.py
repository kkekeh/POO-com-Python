from abc import ABC, abstractmethod

# Para criarmos abstração em Python, precisamos importar o módulo ABC (Abstract Base Class).


class ClasseAbstrata(ABC):  # Classe genérica que não será instanciada.

    @abstractmethod  # Decorador que indica o método abstrato.
    def metodo_abstrato(self):
        pass


class Filha(ClasseAbstrata):
    
    # Implementando o método abstrato (necessário).
    def metodo_abstrato(self):  
        pass


filha = Filha()

# nota: Para que uma classe seja abstratada, ela precisa de, pelo menos, um método abstrato (@abstractmethod).

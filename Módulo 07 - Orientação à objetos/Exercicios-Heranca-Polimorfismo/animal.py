"""
1) Implemente uma superclasse Animal com métodos como emitir_som() e mover(). 
Crie subclasses como Cachorro, Gato, Pássaro. Sobrescreva os métodos para representar o nome específico de cada animal.
"""

class Animal:
    """Animal representa a superclasse de animais."""
    def __init__(self, nome: str, cor: str) -> None:
        """
        Attributes:
            nome (str): Nome do animal
            cor (str): Cor do animal
        """
        self.nome = nome
        self.cor = cor

    def emitir_som(self):
        """Emite o som do animal."""
        print(f"O animal fez um som!")

    def mover(self):
        """Move o animal de lugar """
        print(f"Animal movido!")
    

    

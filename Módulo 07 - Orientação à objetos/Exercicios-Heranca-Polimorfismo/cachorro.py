"""Complemento do exerício 1."""

from animal import Animal

class Cachorro(Animal):
    """Essa subclasse representa um cachorro.

    Attributes:
        nome (str): Nome do animal
        cor (str): Cor do animal
        raca (str): Raça do animal
    """

    def __init__(self, nome: str, cor: str, raca: str) -> None:
        super().__init__(nome, cor)
        self.raca = raca

    def latir(self):
        """Emite o som do cachorro."""
        super().emitir_som()
        print(f"O {self.nome} latiu!")
    
    def mover(self):
        """Move o cachorro de lugar."""
        super().mover()
        print(f"O {self.nome} se locomoveu!")
    
if __name__ == "__main__":
    cachorro_do_Gustavo = Cachorro("Max", "Marrom", "Pinscher")
    cachorro_do_Gustavo.latir()
    cachorro_do_Gustavo.mover()
    cachorro_2 = Cachorro("Teddy", "Preto", "Poodle")
    cachorro_2.latir()
    cachorro_2.mover()
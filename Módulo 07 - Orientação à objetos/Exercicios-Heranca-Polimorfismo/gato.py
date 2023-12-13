"""Complemento exercício 1"""

from animal import Animal

class Gato(Animal):
    """Essa subclasse representa um gato.
    
    Attributes:
        nome (str): Nome do animal
        cor (str): Cor do animal
        raca (str): Raça do animal
    """

    def __init__(self, nome: str, cor: str, raca: str) -> None:
        super().__init__(nome, cor)
        self.raca = raca

    def miar(self):
        """Emite o som do gato."""
        super().emitir_som()
        print(f"O {self.nome} miou!")

    def mover(self):
        """Move o gato de lugar."""
        super().mover()
        print(f"O {self.nome} se locomoveu!")

if __name__ == "__main__":
    gato_do_Gustavo = Gato("Gatito", "Marrom", "Raça1")
    gato_do_Gustavo.miar()
    gato_do_Gustavo.mover()
    gato_2 = Gato("Botinha", "Preto", "Raça2")
    gato_2.miar()
    gato_2.mover()
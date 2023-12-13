"""Complemento do exercício 1"""

from animal import Animal

class Passaro(Animal):
    """Essa subclasse representa um animal.

    Attributes:
        nome (str): Nome do animal
        cor (str): Cor do animal
        raca (str): Raça do animal
    """

    def __init__(self, nome: str, cor: str, raca: str) -> None:
        super().__init__(nome, cor)
        self.raca = raca

    def emitir_som(self):
        """Emite o som do pássaro."""
        print(f"O {self.nome} cantou!")

    def mover(self):
        """Move o pássaro de lugar"""
        print(f"O {self.nome} voou!")


if __name__ == "__main__":
    passaro_do_Gustavo = Passaro("Gatito", "Marrom", "Raça1")
    passaro_do_Gustavo.cantar()
    passaro_do_Gustavo.voar()
    passaro_2 = Passaro("Botinha", "Preto", "Raça2")
    passaro_2.cantar()
    passaro_2.mover()
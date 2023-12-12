"""Implementação da classe Combate."""

from mago import Mago
from guerreiro import Guerreiro
from Heranca_Polimorfismo_Playground import Personagem

class Combate:
    """Combate representa uma partida no jogo.

    Attributes:
        personagem1 (Personagem): Personagem 1.
        personagem2 (Personagem): Personagem 2.
    """


    def __init__(self, personagem1: Personagem, personagem2: Personagem) -> None:
        """
        Inicializa um objeto Combate.

        Args:
            personagem1 (Personagem): Personagem 1.
            personagem2 (Personagem): Personagem 2.
        """
        if not isinstance(personagem1, Personagem):
            raise TypeError("personagem 1 precisa ser do tipo Personagem")
        
        if not isinstance(personagem2, Personagem):
            raise TypeError("personagem 2 precisa ser do tipo Personagem")

        self.personagem1 = personagem1
        self.personagem2 = personagem2

    def iniciar_combate(self) -> None:
        """Inicia o combate entre os dois personagens."""
        print(f"Início do combate entre {self.personagem1} e {self.personagem2}!")

        self.personagem1.atacar()
        self.personagem2.defender()

        self.personagem2.atacar()
        self.personagem1.defender()

        self.personagem1.atacar()
        self.personagem2.morrer()

        print("Fim do combate!")


if __name__ == "__main__":
    guto_mage = Mago("Gustavo Mago", 1 , 10, 10)
    guto_warrior = Guerreiro("Gustavo Guerreiro", 1 , 10, 10)
    combate = Combate(guto_mage, guto_warrior)
    combate.iniciar_combate()
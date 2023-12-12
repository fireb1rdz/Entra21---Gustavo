from Heranca_Polimorfismo_Playground import Personagem

class Mago(Personagem):
    """Mago representa um mago no jogo.
    
    Attributes:
        nome (str): Nome do mago.
        nivel (int): Nível do mago.
        vida (int): Vida do mago.
        magia (int): Quantidade de magia do mago.
    """
    
    def __init__(self, nome: str, nivel: int, vida: int, magia: int):
        super().__init__(nome, nivel, vida)
        self.magia = magia

    def atacar(self):
        """Realiza a ação de ataque do mago."""
        super().atacar()
        print(f"{self.nome} lança um feitiço poderoso com {self.magia} de magia!")

    def equipar_cajado(self):
        """Realiza a ação de equipar o cajado do mago."""
        print(f"{self.nome} equipou o cajado! O próximo ataque causará dano em área.")


if __name__ == "__main__":
    mago = Mago("Gustavo", 2, 10, 10)

    print(mago.nome)
    print(mago.magia)
    mago.atacar()
    mago.equipar_cajado()
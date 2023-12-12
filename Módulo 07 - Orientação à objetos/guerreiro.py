from Heranca_Polimorfismo_Playground import Personagem

class Guerreiro(Personagem):
    """Guerreiro representa um guerreiro no jogo.
    
    Attributes:
        nome (str): Nome do guerreiro.
        nivel (int): Nível do guerreiro.
        vida (int): Vida do guerreiro.
        forca (int): Quantidade de força do guerreiro.
    """
    def __init__(self, nome: str, nivel: int, vida: int, forca: int):
        super().__init__(nome, nivel, vida)
        self.forca = forca
        
    def atacar(self):
        """Realiza a ação de ataque do guerreiro."""
        super().atacar()
        print(f"{self.nome} realiza um poderoso ataque com {self.forca} de força!")

    def equipar_escudo(self):
        """Realiza a ação de equipar o escudo do guerreiro."""
        print(f"{self.nome} equipou o escudo! a vida aumentou em {self.equipar_escudo}.")


if __name__ == "__main__":
    guerreiro = Guerreiro("Gustavo", 2, 10, 10)

    print(guerreiro.nome)
    print(guerreiro.equipar_escudo)
    guerreiro.atacar()
    guerreiro.defender()
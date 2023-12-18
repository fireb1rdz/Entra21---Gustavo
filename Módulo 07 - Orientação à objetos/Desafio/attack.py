class Attack:
    """Ataque representa um ataque.
    
    Attributes:
        name (str): Nome do ataque
        damage (int): Quantidade de dano do ataque
        tipo (str): Tipo do ataque.
    """
    def __init__(self, name: str, damage: int, type: str) -> None:
        self.name = name
        self.damage = damage
        self.type = type
    
    def __repr__(self) -> str:
        return f"{self.name}"

    
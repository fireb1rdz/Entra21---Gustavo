from attack import Attack

class Pokemon:
    """Pokemon representa um pokemon
    
    Attributes:
        nome (str): Nome do pokemon
        tipo (str): Tipo do pokemon
    """
    def __init__(self, name: str, type: str, hp: int, *attacks: Attack) -> None:
        self.name = name
        self.type = type
        self.hp = hp
        self.attacks = [attacks]

    def __str__(self) -> str:
        return f"Name: {self.name} | HP: {self.hp}"

    def __repr__(self) -> str:
        return f"Name: {self.name} | HP: {self.hp}"
    
    def receive_damage(self, damage):
        """Método para receber dano."""
        self.hp -= damage
    
    def verify_hp(self):
        """Verificar se está vivo."""
        if self.hp > 0:
            return True
        return False
    
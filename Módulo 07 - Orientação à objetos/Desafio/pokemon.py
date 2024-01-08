from attack import Attack

class Pokemon:
    """Pokemon represents a Pokemon
    
    Attributes:
        id (int): Pokemon ID
        name (str): Pokemon's name
        type (str): Pokemon's type
        hp (int): Pokemon's health points
        attacks (Attack[list]): List with the Pokemon's attacks
    """
    def __init__(self, id: int, name: str, type: str, hp: int, *attacks: Attack) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.hp = hp
        self.attacks = attacks

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"{self.name}"
    
    def receive_damage(self, damage):
        """Method to receive damage."""
        self.hp -= damage
    
    def verify_hp(self):
        """Verifies if it's alive."""
        if self.hp > 0:
            return True
        return False
    
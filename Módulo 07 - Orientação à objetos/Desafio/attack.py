class Attack:
    """Attack represents an attack.
    
    Attributes:
        name (str): Attack's name
        damage (int): Attack's damage quantity
        type (str): Attack's type
    """
    def __init__(self, id: int, name: str, damage: int, type: str) -> None:
        self.id = id
        self.name = name
        self.damage = damage
        self.type = type
    
    def __repr__(self) -> str:
        return f"{self.name}"
    
    def __str__(self) -> str:
        return f"{self.name}"

    
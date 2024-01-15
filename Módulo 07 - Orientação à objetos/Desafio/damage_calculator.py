class DamageCalculator:
    """DamageCalculator represents a damage calculator.
    
    Attributes:
        defensor_pokemon (Pokemon): The Pokemon that will receive the damage.
        attack (Attack): The attack.

    Returns:
        (int): Damage multiplier.

    """
    type_multiplier = {
        ("electric", "water"): 2, 
        ("water", "fire"): 2,
        ("fire", "plant"): 2,
        ("plant", "dirt") : 2,
        ("dirt", "rock") :2
        }
    
    @staticmethod
    def get_multiplier(attack_type: str, defender_type: str):
        """Calculate the multiplier of an Attack according to the type_multiplier dictionary.
        
        Args:
            attack_type (Attack): The attack type
        
        Returns: 
            defender_type (Pokemon): The defender's pokemon type."""
        return DamageCalculator.type_multiplier.get((attack_type, defender_type), 1)



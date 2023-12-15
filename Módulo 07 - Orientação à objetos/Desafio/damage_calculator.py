class DamageCalculator:
    """DamageCalculator representa uma calculadora de dano de ataque.
    
    Attributes:
        defensor_pokemon (Pokemon): O pokemon que está defendendo.
        attack (Attack): O ataque utilizado.

    Returns:
        (int): Multiplicador de dano.

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
        """Calcula o multiplicador de um ataque"""
        return DamageCalculator.type_multiplier.get((attack_type, defender_type), 1)



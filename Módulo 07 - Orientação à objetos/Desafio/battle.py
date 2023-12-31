from pokemon import Pokemon
from attack import Attack
from damage_calculator import DamageCalculator


class Battle:
    """Battle representa uma batalha.
    
    Attributes:
        user_pokemon (Pokemon): O pokemon escolhido pelo usuário.
        machine_pokemon (Pokemon): O pokemon escolhido pela maquina.
    """
    def __init__(self, user_pokemon: Pokemon, machine_pokemon: Pokemon) -> None:
        self.user_pokemon = user_pokemon
        self.machine_pokemon = machine_pokemon

    def user_turn(self, attack: Attack):
        damage_multiplier = DamageCalculator.get_multiplier(attack.type, self.machine_pokemon.type)
        damage = attack.damage * damage_multiplier
        self.machine_pokemon.receive_damage(damage)
        print(f"\n{self.user_pokemon.name}: {self.user_pokemon.hp} HP")
        print(f"{self.machine_pokemon.name}: {self.machine_pokemon.hp} HP")
        winner = self.battle_end()
        if winner:
            print(f"{self.machine_pokemon} was defeated! {self.user_pokemon} won!")
    
    def machine_turn(self, attack: Attack):
        """machine_turn is called when the machine is going to attack.
        
        Args:
            attack (Attack): The attack the user chose.
        
        Returns: 
            winner (Pokemon): The winner pokemon.
        """
        damage_multiplier = DamageCalculator.get_multiplier(attack.type, self.user_pokemon.type)
        damage = attack.damage * damage_multiplier
        self.user_pokemon.receive_damage(damage)
        print(f"\n{self.user_pokemon.name}: {self.user_pokemon.hp} HP")
        print(f"{self.machine_pokemon.name}: {self.machine_pokemon.hp} HP")
        winner = self.battle_end()
        if winner:
            return winner

    def battle_end(self) -> Pokemon:
        """Verifica se algum dos pokemons foi derrotado."""
        if not self.user_pokemon.verify_hp():
            return self.user_pokemon
        elif not self.machine_pokemon.verify_hp():
            return self.machine_pokemon
        return False

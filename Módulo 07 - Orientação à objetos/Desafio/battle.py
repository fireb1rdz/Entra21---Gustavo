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
        if not self.user_pokemon.verify_hp():
            print(f"The battle has already ended.")
            return
        print(f"Usuário ataca. \nPokemón do usuário: {self.user_pokemon}\nPokemón da máquina: {self.machine_pokemon}\n\n")
        damage_multiplier = DamageCalculator.get_multiplier(attack.type, self.machine_pokemon.type)
        damage = attack.damage * damage_multiplier
        self.machine_pokemon.receive_damage(damage)
        if not self.machine_pokemon.verify_hp():
            print(f"{self.machine_pokemon.name} was defeated! {self.user_pokemon.name} won!")
    
    def machine_turn(self, attack: Attack):
        if not self.machine_pokemon.verify_hp():
            print("The battle has already ended.")
            return
        print(f"Máquina ataca. \nPokemón do usuário: {self.user_pokemon}\nPokemón da máquina: {self.machine_pokemon}\n\n")
        damage_multiplier = DamageCalculator.get_multiplier(attack.type, self.user_pokemon.type)
        damage = attack.damage * damage_multiplier
        self.user_pokemon.receive_damage(damage)
        if not self.user_pokemon.verify_hp():
            print(f"{self.user_pokemon.name} was defeated! {self.machine_pokemon.name} won!")


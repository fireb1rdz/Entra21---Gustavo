from pokemon import Pokemon
from attack import Attack
from damage_calculator import DamageCalculator
from battle import Battle

if __name__ == "__main__":
    investida = Attack("punch", 20, "normal")
    gelo = Attack("icepunch", 20, "ice")
    planta = Attack("plant-attack", 20, "plant")
    fogo = Attack("fireball", 20, "fire")
    pokemon1 = Pokemon("Charizard", "fire", 100, fogo)
    pokemon2 = Pokemon("Squirtle", "plant", 100, planta)
    battle = Battle(pokemon1, pokemon2)
    battle.user_turn(fogo)
    battle.machine_turn(planta)
    battle.user_turn(fogo)
    battle.machine_turn(planta)
    battle.user_turn(fogo)
    battle.machine_turn(planta)

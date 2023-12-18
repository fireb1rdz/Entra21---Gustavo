from pokemon import Pokemon
from attack import Attack
from damage_calculator import DamageCalculator
from battle import Battle
from random import randint

if __name__ == "__main__":
    punch = Attack("punch", 20, "normal")
    water = Attack("waterpunch", 20, "water")
    plantAttack = Attack("plant attack", 20, "plant")
    fireball = Attack("fireball", 20, "fire")
    charizard = Pokemon("Charizard", "fire", 100, fireball, punch)
    squirtle = Pokemon("Squirtle", "plant", 100, plantAttack, punch)
    psyduck = Pokemon("Psyduck", "water", 100, water, punch)
    pokemons = [charizard, squirtle]

    def battle_start():

        user_choice = int(input("""
Welcome to Pokemon Battle 2.0!
          
1) Charizard
2) Squirtle

Choose your Pokemon: """))
        user_pokemon = pokemons[user_choice - 1]
        machine_pokemon = pokemons[randint(0, len(pokemons) - 1)]
        while user_pokemon == machine_pokemon:
            machine_pokemon = pokemons[randint(0, len(pokemons) - 1)]
        battle = Battle(user_pokemon, machine_pokemon)
        round = 2
        while True:
            if round % 2 == 0:
                print(f"""
--------------------------------------------------
User turn - {user_pokemon}
""")
                for number, attack in enumerate(user_pokemon.attacks):
                    print(f"{number + 1}) {attack}")
                user_attack_choice = int(input("\nChoose your attack: ")) - 1
                battle.user_turn(user_pokemon.attacks[user_attack_choice])
                round += 1
            else:
                print(f"""
--------------------------------------------------
Machine turn - {machine_pokemon}
""")
                machine_attack_choice = randint(0, len(machine_pokemon.attacks) - 1)
                print(f"Machine chose {machine_pokemon.attacks[machine_attack_choice]}")
                battle.machine_turn(machine_pokemon.attacks[machine_attack_choice])
                round += 1
            winner = battle.battle_end()
            if winner == user_pokemon:
                print(f"{machine_pokemon} was defeated. {user_pokemon} won!")
                return
            elif winner == machine_pokemon:
                print(f"{user_pokemon} was defeated. {machine_pokemon} won!")
                return

battle_start()
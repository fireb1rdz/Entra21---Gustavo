from pokemon import Pokemon
from attack import Attack
from damage_calculator import DamageCalculator
from battle import Battle
from random import randint
from time import sleep

if __name__ == "__main__":
    punch = Attack("punch", 20, "normal")
    water = Attack("waterpunch", 20, "water")
    plantAttack = Attack("plant attack", 20, "plant")
    fireball = Attack("fireball", 20, "fire")
    charizard = Pokemon(1, "Charizard", "fire", 100, fireball, punch)
    squirtle = Pokemon(2, "Squirtle", "plant", 100, plantAttack, punch)
    psyduck = Pokemon(3, "Psyduck", "water", 100, water, punch)
    pokemons = [charizard, squirtle, psyduck]

    def user_attack_choice(user_pokemon: Pokemon, battle: Battle):
        print(f"User turn - {user_pokemon}")
        for number, attack in enumerate(user_pokemon.attacks):
            print(f"{number + 1}) {attack}")
        user_attack_choice = int(input("\nChoose your attack: "))
        print(f"You chose {user_pokemon.attacks[user_attack_choice - 1]}!")
        round_timer()
        battle.user_turn(user_pokemon.attacks[user_attack_choice - 1])
        return
    
    def machine_attack_choice(machine_pokemon: Pokemon, battle: Battle):
        machine_attack_choice = randint(0, len(machine_pokemon.attacks) - 1)
        print(f"Machine turn - {machine_pokemon}\n")
        print(f"Machine chose {machine_pokemon.attacks[machine_attack_choice]}")
        round_timer()
        battle.machine_turn(machine_pokemon.attacks[machine_attack_choice])
        return

    def round_timer():
        sleep(1)
        print("\n3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)
        return

    def separator():
        print("--------------------------------------------------")

    def battle_start():
        """battle_start starts the battle manipulation"""

        for Pokemon in pokemons:
            print(f"""{Pokemon.id}) {Pokemon.name}""")
        user_choice = int(input("Choose your Pokemon: "))
        user_pokemon = pokemons[Pokemon.id == user_choice] # Defines the user's pokemon
        print(f"You chose {user_pokemon}!")
        machine_pokemon = pokemons[randint(0, len(pokemons) - 1)]  # Defines the machine's pokemon
        while user_pokemon == machine_pokemon: # If machine chose the same as the user, changes
            machine_pokemon = pokemons[randint(0, len(pokemons) - 1)]
        print(f"Machine chose {machine_pokemon}, get ready!")
        battle = Battle(user_pokemon, machine_pokemon) # Create an object with the Battle class
        round = randint(2,3) # Randomizes the initial round
        while True:
            winner = battle.battle_end() # Verifing if there is any winner
            if winner:
                if winner == user_pokemon:
                    print(f"{machine_pokemon} was defeated. {user_pokemon} won!")
                else:
                    print(f"{user_pokemon} was defeated. {machine_pokemon} won!")
                return

            if round % 2 == 0: # Defines whose turn it i
                separator()
                user_attack_choice(user_pokemon, battle)
                round += 1
            else:
                separator()
                machine_attack_choice(machine_pokemon, battle)
                round += 1

battle_start()
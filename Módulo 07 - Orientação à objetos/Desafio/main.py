from pokemon import Pokemon
from attack import Attack
from damage_calculator import DamageCalculator
from battle import Battle
from random import randint
from round_manager import Round
from pokemon_repository import PokemonRepository
from attack_repository import AttackRepository
from pokemon_attack_repository import PokemonAttackRepository

if __name__ == "__main__":
    round = Round() # Creating the Round instance
    pokemon_repository = PokemonRepository("db.db") # Creating the pokemon repository
    pokemons = pokemon_repository.get_pokemons() # Getting all pokemons from the database
    attack_repository = AttackRepository("db.db") # Creating the attack repository
    attacks = attack_repository.get_attacks() # Getting all attacks from the database
    pokemon_attack_repository = PokemonAttackRepository("db.db") # Creating the pokemon x attack repository


    def user_attack_choice(user_pokemon: Pokemon, battle: Battle):
        """ user_attack_choice is called when the user is going to choose the attack.
        
        Args:
            user_pokemon (Pokemon): The user's pokemon.
            battle (Battle): The battle instance.
        """
        print(f"User turn - {user_pokemon}")
        user_attacks = pokemon_attack_repository.get_attacks_by_pokemon_id(user_pokemon) # Getting the attacks of user's pokemon
        for index, attack in enumerate(user_attacks):
            print(f"{index + 1}) {attack}")
        chosen_attack = int(input("Choose your attack: "))
        print(f"You chose {user_attacks[chosen_attack - 1]}!")
        round.timer()
        battle.user_turn(user_attacks[chosen_attack - 1])
        return
    
    def machine_attack_choice(machine_pokemon: Pokemon, battle: Battle):
        machine_attack_choice = randint(0, 3)
        machine_attacks = pokemon_attack_repository.get_attacks_by_pokemon_id(machine_pokemon)
        print(f"Machine turn - {machine_pokemon}\n")
        print(f"Machine chose {(machine_attacks[machine_attack_choice - 1])}")
        round.timer()
        battle.machine_turn(machine_attacks[machine_attack_choice - 1])
        return

    def battle_start():
        """battle_start starts the battle manipulation"""


        for Pokemon in pokemons:
            print(f"""{Pokemon.id}) {Pokemon.name}""")
        user_choice = int(input("Choose your Pokemon: "))
        user_pokemon = pokemons[user_choice - 1] # Defines the user's pokemon
        print(f"You chose {user_pokemon}!")
        machine_pokemon = pokemons[randint(0, len(pokemons) - 1)]  # Defines the machine's pokemon
        while user_pokemon == machine_pokemon: # If machine chose the same as the user, changes
            machine_pokemon = pokemons[randint(0, len(pokemons) - 1)]
        print(f"Machine chose {machine_pokemon}, get ready!")
        battle = Battle(user_pokemon, machine_pokemon) # Create an object with Battle class
        while True:
            winner = battle.battle_end() # Verifing if there is any winner
            if winner:
                if winner == user_pokemon:
                    print(f"{machine_pokemon} was defeated. {user_pokemon} won!")
                else:
                    print(f"{user_pokemon} was defeated. {machine_pokemon} won!")
                return

            if round.round % 2 == 0: # Defines whose turn it i
                round.separator()
                user_attack_choice(user_pokemon, battle)
                round.next()
            else:
                round.separator()
                machine_attack_choice(machine_pokemon, battle)
                round.next()

battle_start()
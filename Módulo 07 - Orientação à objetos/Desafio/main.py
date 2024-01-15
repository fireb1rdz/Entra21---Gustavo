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
        for index, attack in enumerate(user_attacks): # Iterating in the attacks
            print(f"{index + 1}) {attack}") # Printing index + attack
        chosen_attack = int(input("\nChoose your attack: ")) # Asking the user to put the attack index
        print(f"You chose {user_attacks[chosen_attack - 1]}!")
        round.timer() # Starting the timer
        battle.user_turn(user_attacks[chosen_attack - 1]) # Calling user_turn method
        return
    
    def machine_attack_choice(machine_pokemon: Pokemon, battle: Battle):
        """ machine_attack_choice is called when the machine is going to choose the attack.
        
        Args:
            machine_pokemon (Pokemon): The machine's pokemon.
            battle (Battle): The battle instance.
        """
        machine_attack_choice = randint(0, 3) # Randomizing the choice
        machine_attacks = pokemon_attack_repository.get_attacks_by_pokemon_id(machine_pokemon) # Getting the attacks according to machine's pokemon.
        print(f"Machine turn - {machine_pokemon}\n")
        print(f"Machine chose {(machine_attacks[machine_attack_choice - 1])}") # Printing the chosen attack
        round.timer() # Starting the timer
        battle.machine_turn(machine_attacks[machine_attack_choice - 1]) # Calling machine_turn method
        return

    def battle_start():
        """battle_start starts the battle manipulation"""

        for Pokemon in pokemons: 
            print(f"""{Pokemon.id}) {Pokemon.name}""") # Printing the pokemons in the database
        user_choice = int(input("Choose your Pokemon: ")) # Asking the user to choose a pokemon
        user_pokemon = pokemons[user_choice - 1] # Defines the user's pokemon
        print(f"You chose {user_pokemon}!")
        machine_pokemon = pokemons[randint(0, len(pokemons) - 1)]  # Randomly defines the machine's pokemon
        while user_pokemon == machine_pokemon: # If machine chose the same as the user, changes
            machine_pokemon = pokemons[randint(0, len(pokemons) - 1)]
        print(f"Machine chose {machine_pokemon}, get ready!")
        battle = Battle(user_pokemon, machine_pokemon) # Create an object with Battle class
        while True: # While there is no winner, continues
            winner = battle.battle_end() # Verifing if there is any winner
            if winner: # If there is a winner, makes the conditionals
                if winner == user_pokemon:
                    print(f"{machine_pokemon} was defeated. {user_pokemon} won!")
                else:
                    print(f"{user_pokemon} was defeated. {machine_pokemon} won!")
                return

            if round.round % 2 == 0: # Defines whose turn it is
                round.separator() # Prints the separator (-)
                user_attack_choice(user_pokemon, battle) # Calling the user_attack_choice method
                round.next() # Skipping the round
            else:
                round.separator() # Prints the separator (-)
                machine_attack_choice(machine_pokemon, battle) # Calling the machine_attack_choice method
                round.next() # Skipping the round

battle_start()
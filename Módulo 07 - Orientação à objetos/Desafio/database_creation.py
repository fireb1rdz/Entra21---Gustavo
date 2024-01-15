from database_starter import BDStarter
from pokemon_repository import PokemonRepository
from attack_repository import AttackRepository
from pokemon_attack_repository import PokemonAttackRepository
from pokemon import Pokemon
from attack import Attack

# # Initializing BD
DB_NAME = "db.db"
BDStarter.create_tables(DB_NAME)

# # Initializing the repositories
pokemon_repository = PokemonRepository(DB_NAME)
attack_repository = AttackRepository(DB_NAME)
pokemon_attack_repository = PokemonAttackRepository(DB_NAME)

# Creating the Attack instances

attack1 = Attack(1, "Flame Thrower", 140, "fire")
attack2 = Attack(2, "Wing Attack", 70, "flying")
attack3 = Attack(3, "Flame Charge", 50, "fire")
attack4 = Attack(4, "Ember", 30, "fire")
attack5 = Attack(5, "Hyper Whirlpool", 80, "water")
attack6 = Attack(6, "Water Gun", 30, "water")
attack7 = Attack(7, "Tackle", 10, "normal")
attack8 = Attack(8, "Pollen Hazard", 50, "grass")
attack9 = Attack(9, "Poison Powder", 60, "grass")
attack10 = Attack(10, "Whirlwind", 60, "normal")
attack11 = Attack(11, "Mach Cyclone", 130, "flying")
attack12 = Attack(12, "Feather Dance", 70, "flying")
attack13 = Attack(13, "Electric Surfer", 80, "electric")
attack14 = Attack(14, "Thunder", 160, "electric")
attack15 = Attack(15, "Pain-Full Punch", 40, "normal")

# Creating pokemons instances
pokemon1 = Pokemon(1, "Charizard", "fire", 250)
pokemon2 = Pokemon(2, "Blastoise", "water", 240)
pokemon3 = Pokemon(3, "Venusaur", "grass", 220)
pokemon4 = Pokemon(4, "Pidgeot", "flying", 170)
pokemon5 = Pokemon(5, "Raichu", "Electric", 210)

# Inserting the attacks
attack_repository.insert_attack(attack1)
attack_repository.insert_attack(attack2)
attack_repository.insert_attack(attack3)
attack_repository.insert_attack(attack4)
attack_repository.insert_attack(attack5)
attack_repository.insert_attack(attack6)
attack_repository.insert_attack(attack7)
attack_repository.insert_attack(attack8)
attack_repository.insert_attack(attack9)
attack_repository.insert_attack(attack10)
attack_repository.insert_attack(attack11)
attack_repository.insert_attack(attack12)
attack_repository.insert_attack(attack13)
attack_repository.insert_attack(attack14)
attack_repository.insert_attack(attack15)

# Inserting the pokemons
pokemon_repository.insert_pokemon(pokemon1)
pokemon_repository.insert_pokemon(pokemon2)
pokemon_repository.insert_pokemon(pokemon3)
pokemon_repository.insert_pokemon(pokemon4)
pokemon_repository.insert_pokemon(pokemon5)

# Inserting the Pokemons X Attacks references
pokemon_attack_repository.insert_pokemon_attack_relation(1, 1, 1)
pokemon_attack_repository.insert_pokemon_attack_relation(2, 1, 2)
pokemon_attack_repository.insert_pokemon_attack_relation(3, 1, 3)
pokemon_attack_repository.insert_pokemon_attack_relation(4, 2, 4)
pokemon_attack_repository.insert_pokemon_attack_relation(5, 2, 5)
pokemon_attack_repository.insert_pokemon_attack_relation(6, 2, 6)
pokemon_attack_repository.insert_pokemon_attack_relation(7, 3, 7)
pokemon_attack_repository.insert_pokemon_attack_relation(8, 3, 8)
pokemon_attack_repository.insert_pokemon_attack_relation(9, 3, 9)
pokemon_attack_repository.insert_pokemon_attack_relation(10, 4, 10)
pokemon_attack_repository.insert_pokemon_attack_relation(11, 4, 11)
pokemon_attack_repository.insert_pokemon_attack_relation(12, 4, 12)
pokemon_attack_repository.insert_pokemon_attack_relation(13, 5, 13)
pokemon_attack_repository.insert_pokemon_attack_relation(14, 5, 14)
pokemon_attack_repository.insert_pokemon_attack_relation(15, 5, 15)

from database_starter import BDStarter
from pokemon_repository import PokemonRepository
from pokemon import Pokemon
from attack import Attack

# # Inicializando BD
DB_NOME = "pokemons.db"
BDStarter.create_tables(DB_NOME)

# # Inicializando o repositório
pokemon_repository = PokemonRepository(DB_NOME)

# Attack creation

attack1 = Attack("Flame Thrower", 140, "fire")
attack2 = Attack("Wing Attack", 70, "flying")
attack3 = Attack("Flame Charge", 50, "fire")
attack4 = Attack("Ember", 30, "fire")
attack5 = Attack("Hyper Whirlpool", 80, "water")
attack6 = Attack("Water Gun", 30, "water")
attack7 = Attack("Tackle", 10, "normal")
attack8 = Attack("Pollen Hazard", 50, "grass")
attack9 = Attack("Poison Powder", 60, "grass")

# Criando instâncias dos usuários
pokemon1 = Pokemon(1, "Charizard", "fire", 100, attack1.type)
pokemon2 = Pokemon(2, "Blastoise", "water", 100, attack2.type)
pokemon3 = Pokemon(3, "Venusaur", "grass", 100, attack3.type)

print(pokemon1.type)

# Inserindo usuários
pokemon_repository.insert_pokemon(pokemon1, attack1)
pokemon_repository.insert_pokemon(pokemon2, attack2)


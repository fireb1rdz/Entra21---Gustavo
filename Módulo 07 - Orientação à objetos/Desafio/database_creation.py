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

attack1 = Attack("fireball", 20, "fire")
attack2 = Attack("waterfall", 20, "water")

# Criando instâncias dos usuários
pokemon1 = Pokemon(1, "Charizard", "fire", 100, attack1.type)
pokemon2 = Pokemon(2, "Squirtle", "water", 100, attack2.type)

print(pokemon1.type)

# Inserindo usuários
pokemon_repository.insert_pokemon(pokemon1, attack1)
pokemon_repository.insert_pokemon(pokemon2, attack2)

# # print(usuario1, usuario2)

# # Atualizando usuário
# usuario1.email = "email@atualizado.com"
# pokemon_repository.insert_pokemon(usuario1)

# # Removendo usuário
# usuario_repositorio.remover_usuario(usuario2)

# Consultando usuários

"""
Repositório é uma classe responsável por lidar com a persistência e recuperação
de dados em uma fonte de armazenamento, como um banco de dados, arquivo ou serviço
externo.
"""
from typing import Any, List
import sqlite3
from pokemon import Pokemon
from attack import Attack

class PokemonRepository:
    """Pokemon repository."""
    def __init__(self, db_nome: str) -> None:
        self.db_nome = db_nome

    def __execute_query(self, query: str, *params: Any) -> None:
        """Executes a query in the database.
        
        Args:
            query (str): Query that will be executed.
            params (Any): Query parameters.
        """
        connection = sqlite3.connect(self.db_nome)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()

    def insert_pokemon(self, pokemon: Pokemon, attack: Attack) -> Pokemon:
        """Insert a pokemon into the database. The Pokemon object is updated with the database ID.
        
        Args:
            pokemon (Pokemon): Pokemon that will be created.
        """
        query = "INSERT INTO pokemons (id, name, type, hp, attacks) VALUES (?, ?, ?, ?, ?)"
        self.__execute_query(query, pokemon.id, pokemon.name, pokemon.type, pokemon.hp, attack.type)

        pokemon_id = self.get_last_inserted_id()
        print(pokemon_id)
        pokemon.id = pokemon_id

        return pokemon

    def update_pokemon(self, pokemon: Pokemon) -> None:
        """Update the Pokemon's data from the database"""
        query = "UPDATE pokemons SET name = ?, type = ? , hp = ?, attacks = ? WHERE id = ?"
        self.__execute_query(query, pokemon.name, pokemon.type, pokemon.hp, pokemon.attacks, pokemon.id)

    def remove_pokemon(self, pokemon: Pokemon) -> None:
        """Remove a Pokemon from the database."""
        query = "DELETE FROM pokemons WHERE id = ?"
        self.__execute_query(query, pokemon.id)

    def get_pokemons(self) -> List[Pokemon]:
        """Retrieve all users registered in the database."""
        query = "SELECT * FROM pokemons"
        connection = sqlite3.connect(self.db_nome)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        return [Pokemon(row[0], row[1], row[2], row[3], row[4]) for row in rows]
    
    def get_last_inserted_id(self) -> int:
        """Retrieve the ID of the last record inserted into the database."""
        query = "SELECT id FROM pokemons ORDER BY 1 DESC LIMIT 1;"
        connection = sqlite3.connect(self.db_nome)
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        connection.close()
        return row[0]
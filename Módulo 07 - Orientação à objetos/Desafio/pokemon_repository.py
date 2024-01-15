from typing import Any, List
import sqlite3
from pokemon import Pokemon

class PokemonRepository:
    """Pokemon repository."""
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name

    def __execute_query(self, query: str, *params: Any) -> None:
        """Executes a query in the database.
        
        Args:
            query (str): Query that will be executed.
            params (Any): Query parameters.
        """
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()

    def insert_pokemon(self, pokemon: Pokemon) -> Pokemon:
        """Insert a pokemon into the database. The Pokemon object is updated with the database ID.
        
        Args:
            pokemon (Pokemon): Pokemon that will be created.
        """
        query = "INSERT INTO pokemons (id, name, type, hp) VALUES (?, ?, ?, ?)"
        self.__execute_query(query, pokemon.id, pokemon.name, pokemon.type, pokemon.hp)

        return pokemon

    def update_pokemon(self, pokemon: Pokemon) -> None:
        """Update the Pokemon's data from the database"""
        query = "UPDATE pokemons SET name = ?, type = ? , hp = ?, WHERE id = ?"
        self.__execute_query(query, pokemon.name, pokemon.type, pokemon.hp, pokemon.id)

    def remove_pokemon(self, pokemon: Pokemon) -> None:
        """Remove a Pokemon from the database."""
        query = "DELETE FROM pokemons WHERE id = ?"
        self.__execute_query(query, pokemon.id)

    def get_pokemons(self) -> List[Pokemon]:
        """Retrieve all users registered in the database."""
        query = "SELECT * FROM pokemons"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        return [Pokemon(row[0], row[1], row[2], row[3]) for row in rows]
    
from battle import Battle
from pokemon import Pokemon
import sqlite3
from typing import Any

class RegisterRepository:
    """This class represents the battle registers repository"""

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

    def insert_register(self, winner_pokemon: Pokemon, loser_pokemon: Pokemon, date: str) -> None:
        """Inserts a battle register into registers table."""
        query = "INSERT INTO results (winner_pokemon, loser_pokemon, date) VALUES (?, ?, ?)"
        self.__execute_query(query, winner_pokemon.name, loser_pokemon.name, date)
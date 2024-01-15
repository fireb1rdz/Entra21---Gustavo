"""
Class responsible for creating the database and necessary tables to store the data. 
It is a class that follows the Single Responsibility Principle by encapsulating the logic for initializing the database.
"""

import sqlite3

class BDStarter:
    """Class responsible for initializing the database"""
    @staticmethod
    def create_tables(db_name: str):
        """Create tables in the database.

        Args:
            db_name (str): Database name.
        """

        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS pokemons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                hp INTEGER NOT NULL
            );
            CREATE TABLE IF NOT EXISTS attacks (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                damage INTEGER NOT NULL,
                type TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS pokemons_attacks (
                id INTEGER PRIMARY KEY, 
                pokemon_id INTEGER NOT NULL, 
                attack_id INTEGER NOT NULL,
                FOREIGN KEY(pokemon_id) REFERENCES pokemons(id),
                FOREIGN KEY(attack_id) REFERENCES attacks(id)
                )
        """)
        connection.commit()
        connection.close()
    
if __name__ == "__main__":
    BDStarter.create_tables("db.db")
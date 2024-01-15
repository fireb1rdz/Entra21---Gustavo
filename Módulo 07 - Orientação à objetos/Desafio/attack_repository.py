from typing import Any, List
import sqlite3
from attack import Attack

class AttackRepository:
    """Attack repository."""
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

    def insert_attack(self, attack: Attack) -> Attack:
        """Insert a attack into the database. The Attack object is updated with the database ID.
        
        Args:
            attack (Attack): Attack that will be created.
        """
        query = "INSERT INTO attacks (id, name, damage, type) VALUES (?, ?, ?, ?)"
        self.__execute_query(query, attack.id, attack.name, attack.damage, attack.type)

        return attack

    def update_attack(self, attack: Attack) -> None:
        """Update the Attack's data from the database"""
        query = "UPDATE attacks SET name = ?, damage = ? , type = ?, WHERE id = ?"
        self.__execute_query(query, attack.name, attack.damage, attack.type, attack.id)

    def remove_attack(self, attack: Attack) -> None:
        """Remove a Attack from the database."""
        query = "DELETE FROM attacks WHERE id = ?"
        self.__execute_query(query, attack.id)

    def get_attacks(self) -> List[Attack]:
        """Retrieve all users registered in the database."""
        query = "SELECT * FROM attacks"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        return [Attack(row[0], row[1], row[2], row[3]) for row in rows]
    
    
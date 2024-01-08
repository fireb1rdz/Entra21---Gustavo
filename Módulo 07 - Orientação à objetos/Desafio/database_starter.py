"""
Classe responsável por criar o banco de dados e as tabelas necessárias para armazenar 
os dados. É uma classe que segue o princípio de responsabilidade única ao encapsular
a lógica de inicialização do banco de dados.
"""

import sqlite3

class BDStarter:
    """Class responsible for initializing the database"""
    @staticmethod
    def create_tables(db_name: str):
        """Cria as tabelas no banco de dados.

        Args:
            db_nome (str): Nome do banco de dados.
        """

        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pokemons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                hp INTEGER NOT NULL,
                attacks TEXT NOT NULL
            );
        """)
        connection.commit()
        connection.close()
    
if __name__ == "__main__":
    BDStarter.create_tables("pokemons")
"""
2) Implemente a classe Aluno que possua os atributos: número de matrícula, nome, notas. Essa classe deve conter os seguintes métodos: 
get_media() - Calcula a média do aluno com base nas notas.
get_situacao() - Informa a situação do aluno com base no critérios:
0 à 4 - Reprovado
5 à 6 - Recuperação
7 à 10 - Aprovado
"""

class Aluno:
    """Aluno representa um aluno
    
    Attributes:
        name (str): Nome do aluno
        grades (List[float]): Notas do aluno
    """
    def __init__(self, numero_matricula: str, nome: str, notas: list) -> None:
        
        self.__numero_matricula = numero_matricula
        self.nome = nome
        self.notas = notas
    
    @property
    def numero_matricula(self):
        """str: Numero da matrícula."""
        return self.__numero_matricula

    def get_media(self):
        """Retorna a media das notas do aluno.

        Returns:
            float: media de notas do aluno
        """

        return sum(self.notas) / len(self.notas)

    def get_situacao(self):
        """Verifica e retorna a situação de um aluno.
        0 à 4 - Reprovado
        5 à 6 - Recuperação
        7 à 10 - Aprovado

        Returns:
            str: Retorna a palavra conforme condição.
        """

        if self.get_media() <= 4:
            return f"Reprovado!"
        elif self.get_media() <= 6:
            return f"Recuperação!"
        elif self.get_media() <= 10:
            return f"Aprovado!"
    
if __name__ == "__main__":
    gustavo = Aluno(123123, "Gustavo", [10, 2, 2])
    print(f"""
Matrícula: {gustavo.numero_matricula}
Nome: {gustavo.nome} 
Notas: {gustavo.notas}
""")
    gustavo.get_media()
    print(gustavo.get_situacao())
    gustavo.__numero_matricula = 0
    print(gustavo.numero_matricula)
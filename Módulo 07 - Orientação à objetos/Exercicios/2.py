"""
2) Implemente a classe Aluno que possua os atributos: número de matrícula, nome, notas. Essa classe deve conter os seguintes métodos: 
get_media() - Calcula a média do aluno com base nas notas.
get_situacao() - Informa a situação do aluno com base no critérios:
0 à 4 - Reprovado
5 à 6 - Recuperação
7 à 10 - Aprovado
"""

class Aluno:
    """Aluno representa um aluno"""
    def __init__(self, numero_matricula: str, nome: str, notas: list) -> None:
        
        self.numero_matricula = numero_matricula
        self.nome = nome
        self.notas = notas
    
    @property
    def numero_matricula(self):
        """str: Numero da matrícula."""
        return self.__numero_matricula
    
    @numero_matricula.setter
    def numero_matricula(self, numero_matricula):
        self.__numero_matricula = numero_matricula
    
    @property
    def nome(self):
        """str: Nome do aluno."""
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome
    
    @property
    def notas(self):
        """str: Nome do aluno."""
        return self.__notas

    @notas.setter
    def notas(self, novas_notas: list):
        self.__notas = novas_notas

    def get_media(self):
        """Retorna a media das notas do aluno.

        Returns:
            float: media de notas do aluno
        """

        soma = sum(self.notas)
        media = soma / len(self.notas)
        return(media)

    def get_situacao(self):
        """Verifica e retorna a situação de um aluno.
        0 à 4 - Reprovado
        5 à 6 - Recuperação
        7 à 10 - Aprovado

        Returns:
            : True caso o número de telefone seja válido, False caso não seja.
        """

        if self.get_media() <= 4:
            return f"Reprovado!"
        elif self.get_media() <= 6:
            return f"Recuperação!"
        elif self.get_media() <= 10:
            return f"Aprovado!"
    
if __name__ == "__main__":
    gustavo = Aluno(123123, "Gustavo", [10, 5, 8])
    print(f"""
Matrícula: {gustavo.numero_matricula}
Nome: {gustavo.nome} 
Notas: {gustavo.notas}
""")
    gustavo.get_media()
    print(gustavo.get_situacao())
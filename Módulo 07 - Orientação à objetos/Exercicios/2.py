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
        return self.__numero_matricula
    
    @numero_matricula.setter
    def numero_matricula(self, numero_matricula):
        self.__numero_matricula = numero_matricula
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, notas: list):
        self.__notas = notas

    def get_media(self):
        # i = 0
        # for i in self.notas:
        #     print(i)
        #     i += i
        #     print(i)
        soma = sum(self.notas)
        media = soma / len(self.notas)
        return(media)

    def get_situacao(self):
        if self.get_media() <= 4:
            print("Reprovado!")
        elif self.get_media() <= 6:
            print("Recuperação!")
        elif self.get_media() <= 10:
            print("Aprovado!")
    
if __name__ == "__main__":
    gustavo = Aluno(123123, "Gustavo", [10, 5, 8])
    print(f"""
Matrícula: {gustavo.numero_matricula}
Nome: {gustavo.nome} 
Notas: {gustavo.notas}
""")
    gustavo.get_media()
    gustavo.get_situacao()
"""
7) Crie uma classe chamada Universidade que representa uma universidade com os seguintes atributos estáticos:
Total de estudantes (int)
Total de professores (int)

A classe deve ter os seguintes métodos estáticos:
Um método matricular_estudante que incrementa o total de estudantes.
Um método contratar_professor que incrementa o total de professores.
Um método obter_total_pessoas que retorna o total de estudantes e professores juntos.
"""

class Universidade:
    """Essa classe representa uma universidade"""

    def __init__(self, total_estudantes: int, total_professores: int) -> None:    
        """
        Args:
            total_estudantes (int): Total de estudantes
            total_professores (int): Total de professores
        """
        self.total_estudantes = total_estudantes
        self.total_professores = total_professores

    def matricular_estudante(self):
        """Adiciona um estudante no valor total de estudantes do objeto."""
        self.total_estudantes += 1
    
    def contratar_professor(self):
        """Adiciona um professor no valor total de professores do objeto."""
        self.total_professores += 1
    
    def obter_total_pessoas(self):
        """Obtém o valor total de pessoas do objeto
        
        Returns:
            int: Valor total das pessoas presentes no objeto.
        """
        return self.total_professores + self.total_estudantes

if __name__ == "__main__":
    cambridge = Universidade(10, 2)
    cambridge.matricular_estudante()
    cambridge.contratar_professor()
    print(cambridge.obter_total_pessoas())

    

"""
9) Crie uma classe chamada Pessoa com os seguintes atributos:
Nome (str)
Idade (int)
A classe deve ter um atributo estático privado chamado total_pessoas para contar o número total de instâncias da classe Pessoa.

Implemente um método estático chamado get_total_pessoas() que retorna o valor do atributo total_pessoas.
"""

class Pessoa:

    total_pessoas = 0

    def __init__(self, nome: str, idade: int) -> None:
        """Essa classe representa uma pessoa"""
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas += 1
    
    def get_total_pessoas() -> None:
        """Retorna a quantidade total de instâncias da classe Pessoa
        
        Returns:
            total_pessoas (int): Quantidade total de instâncias da classe.
        """
        return Pessoa.total_pessoas
    
if __name__ == "__main__":
    gustavo = Pessoa("Gustavo", 18)
    gustavo = Pessoa("Sabrina", 23)
    print(Pessoa.get_total_pessoas())
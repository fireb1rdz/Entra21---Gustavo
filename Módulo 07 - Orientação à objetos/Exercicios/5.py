"""
5) Crie uma classe Calculadora que implemente os métodos estáticos: soma, subtracacao, multiplicacao e divisao.
"""

class Calculadora:
    """Essa classe representa uma calculadora"""

    def __init__(self, nome: str) -> None:
        """Classe.
        
        Args:
            nome (str): Nome da calculadora.
        """
        self.nome = nome

    def soma(self, valor1, valor2):
        """Realiza a soma dos valores informados como parâmetro.
        
        Args:
            valor1 (int): Primeiro valor da soma.
            valor2 (int): Segundo valor da soma.

        Returns:
            int: retorna o resultado da soma dos valores.
        """
        return valor1 + valor2
    
    def subtracao(self, valor1, valor2):
        """Realiza a subtração dos valores informados como parâmetro.
        
        Args:
            valor1 (int): Primeiro valor da subtração.
            valor2 (int): Segundo valor da subtração.

        Returns:
            int: retorna o resultado da subtração dos valores.
        """
        return valor1 - valor2
    
    def multiplicacao(self, valor1, valor2):
        """Realiza a multiplicação dos valores informados como parâmetro.
        
        Args:
            valor1 (int): Primeiro valor da multiplicação.
            valor2 (int): Segundo valor da multiplicação.

        Returns:
            int: retorna o resultado da multiplicação dos valores.
        """
        return valor1 * valor2
    
    def divisao(self, valor1, valor2):
        """Realiza a divisão dos valores informados como parâmetro.
        
        Args:
            valor1 (int): Dividendo.
            valor2 (int): Divisor.

        Returns:
            int: retorna o resultado da divisão dos valores.
        """
        return valor1 / valor2

if __name__ == "__main__":
    calculadora_gustavo = Calculadora("Calculadora do Gustavo")
    print(calculadora_gustavo.soma(1,5))
    print(calculadora_gustavo.subtracao(10,3))
    print(calculadora_gustavo.multiplicacao(10,3))
    print(f"{calculadora_gustavo.divisao(10,3):.2f}")

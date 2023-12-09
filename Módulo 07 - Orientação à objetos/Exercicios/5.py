"""
5) Crie uma classe Calculadora que implemente os métodos estáticos: soma, subtracacao, multiplicacao e divisao.
"""

class Calculadora:
    """Essa classe representa uma calculadora"""

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def soma(self, valor1, valor2):
        return valor1 + valor2
    
    def subtracao(self, valor1, valor2):
        return valor1 - valor2
    
    def multiplicacao(self, valor1, valor2):
        return valor1 * valor2
    
    def divisao(self, valor1, valor2):
        return valor1 / valor2

if __name__ == "__main__":
    calculadora_gustavo = Calculadora("Calculadora do Gustavo")
    print(calculadora_gustavo.soma(1,5))
    print(calculadora_gustavo.subtracao(10,3))
    print(calculadora_gustavo.multiplicacao(10,3))
    print(f"{calculadora_gustavo.divisao(10,3):.2f}")

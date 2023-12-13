"""Complemento do exercício 2."""

from formageometrica import FormaGeometrica

class Retangulo(FormaGeometrica):
    """Essa subclasse representa um retângulo.
    
    Attributes:
        base (float): O valor da base do retângulo.
        altura (float): O valor da altura do retângulo.
    """
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Método para calcular a área do retângulo"""
        print(f"A área do retângulo é {self.base * self.altura}")
    
    def calcular_perimetro(self):
        """Método para calcular o perímetro do retângulo"""
        print(f"O perímetro do retângulo é {2 * (self.base + self.altura)}")
    

if __name__ == "__main__":
    retangulo1 = Retangulo(10, 15)
    retangulo1.calcular_area()
    retangulo1.calcular_perimetro()
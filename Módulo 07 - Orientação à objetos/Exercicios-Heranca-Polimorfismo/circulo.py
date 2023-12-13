"""Complemento exercício 2."""

from formageometrica import FormaGeometrica

class Circulo(FormaGeometrica):
    """Essa subclasse representa um círculo.
    
    Attributes:
        raio (float): O valor do raio do círculo.
    """
    def __init__(self, raio: float) -> None:
        super().__init__()
        self.raio = raio

    def calcular_area(self):
        print(f"A área do círculo é {3.14 * self.raio**2:.2f}")
    
    def calcular_perimetro(self):
        print(f"O perímetro do círculo é {2 * 3.14 * self.raio:.2f}")
    

if __name__ == "__main__":
    circulo1 = Circulo(10)
    circulo1.calcular_area()
    circulo1.calcular_perimetro()
"""Complemento do exercício 2."""

from formageometrica import FormaGeometrica

class Triangulo(FormaGeometrica):
    """Essa subclasse representa um triângulo.
    
    Attributes:
        base (float): Valor da base do triângulo.
        altura (float): Valor da altura do triângulo.
    """
    def __init__(self, base: float, altura: float, lado1= 0, lado2= 0, lado3= 0) -> None:
        super().__init__()
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        """Método para calcular a área do triângulo"""
        print(f"O resultado é {(self.base * self.altura) / 2}")

    def calcular_perimetro(self, lado1=0.0, lado2=0.0, lado3=0.0):
        """Método para calcular o perímetro do triângulo
        
        Args:
            lado1 (float): Lado 1 do triângulo
            lado2 (float): Lado 2 do triângulo
            lado3 (float): Lado 3 do triângulo
        """
        if lado1 + lado2 + lado3 == 0:
            print("Não é possível calcular o perímetro com apenas essas informações.")
        else:
            print(f"O perímetro do triângulo é {lado1 + lado2 + lado3}")


if __name__ == "__main__":
    triangulo1 = Triangulo(10, 15)
    triangulo1.calcular_area()
    triangulo1.calcular_perimetro()
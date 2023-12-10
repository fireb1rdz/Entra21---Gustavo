"""
10) Crie uma classe chamada Triangulo com os seguintes atributos:
Lado1 (float)
Lado2 (float)
Lado3 (float)

A classe deve ter um método chamado verificar_tipo que verifica e retorna o tipo do triângulo com base nos valores dos lados. Os tipos de triângulos podem ser: equilátero, isósceles ou escaleno.
"""

class Triangulo:
    """Essa classe representa um triângulo"""

    def __init__(self, lado1: float, lado2: float, lado3: float) -> None:
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def verificar_tipo(self) -> str:
        if self.lado1 == self.lado2 == self.lado3:
            return f"Esse triângulo é equilátero."
        
        if self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return f"Esse triângulo é isósceles."
        
        else:
            return f"Esse triângulo é escaleno"
        

if __name__ == "__main__":
    triangulo1 = Triangulo(10, 19, 12)
    triangulo2 = Triangulo(10, 10, 12)
    triangulo3 = Triangulo(10, 10, 10)
    print(triangulo1.verificar_tipo())
    print(triangulo2.verificar_tipo())
    print(triangulo3.verificar_tipo())
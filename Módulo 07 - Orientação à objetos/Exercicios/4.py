"""
4) Crie uma classe chamada Ponto2D para representar um ponto no espaço cartesiano. 

Essa classe deve ter os atributos: x e y.
Essa classe deve ter o método estático tem_eixo_comum(ponto_a, ponto_b) que retorna True se dois objetos tiverem as mesmas coordenadas para algum dos eixos.

"""

class Ponto2D:
    """Essa classe representa um ponto no espaço cartesiano"""

    def __init__(self, x, y) -> None:
        """Método construtor da classe.
        
        Args:
            x (int): Ponto x que será adicionado.
            y (int): Ponto y que será adicionado.
        """
        
        self.x_y = x, y

    def tem_eixo_comum(self, x: int, y: int):
        """Verifica se o ponto definido possui um eixo comum com os pontos informados como parâmetro.
        
        Args:
            x (int): Ponto x que será comparado.
            y (int): Ponto y que será comparado.

        Returns:
            bool: retorna True se houver um eixo comum, retorna False se não houver.
        """
        xa, ya = self.x_y
        xb, yb = x, y

        return xa == xb or ya == yb

if __name__ == "__main__":
    coordenadas1 = Ponto2D(3, 5)
    print(coordenadas1.tem_eixo_comum(2,5))
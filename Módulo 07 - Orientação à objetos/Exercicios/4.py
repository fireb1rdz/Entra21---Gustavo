"""
4) Crie uma classe chamada Ponto2D para representar um ponto no espaço cartesiano. 

Essa classe deve ter os atributos: x e y.
Essa classe deve ter o método estático tem_eixo_comum(ponto_a, ponto_b) que retorna True se dois objetos tiverem as mesmas coordenadas para algum dos eixos.

"""
from __future__ import annotations
class Ponto2D:
    """Essa classe representa um ponto no espaço cartesiano"""

    def __init__(self, x: int, y: int) -> None:
        """Método construtor da classe.
        
        Args:
            x (int): Ponto x que será adicionado.
            
            y (int): Ponto y que será adicionado.
        """
        
        self.xa = x
        self.ya = y
    
    @staticmethod
    def tem_eixo_comum(pontoA: Ponto2D, pontoB: Ponto2D):
        """Verifica se o ponto definido possui um eixo comum com os pontos informados como parâmetro.
        
        Args:
            x (int): Ponto x que será comparado.
            y (int): Ponto y que será comparado.

        Returns:
            bool: retorna True se houver um eixo comum, retorna False se não houver.
        """

        return pontoA.xa == pontoB.xa or pontoA.ya == pontoB.ya

if __name__ == "__main__":
    coordenadas1 = Ponto2D(3, 5)
    coordenadas2 = Ponto2D(1, 5)

    print(Ponto2D.tem_eixo_comum(coordenadas1, coordenadas2))
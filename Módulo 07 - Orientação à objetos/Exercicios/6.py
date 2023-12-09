"""
6) Crie uma classe chamada Carro que represente um carro com os seguintes atributos:
Marca (String)
Modelo (String)
Ano (int)
Velocidade (int)

A classe deve ter os seguintes métodos:
Um método construtor que recebe os valores iniciais para marca, modelo e ano, e inicializa a velocidade com 0.
Um método "acelerar" que aumenta a velocidade do carro em 10 unidades.
Um método "frear" que diminui a velocidade do carro em 5 unidades.

"""
class Carro:
    """Essa classe representa um carro"""

    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        """Classe.
        
        Args:
            marca (str): Nome da marca do carro.
            modelo (str): Nome do modelo do carro.
            ano (int): Ano de fabricação do carro.
        """
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def acelerar(self):
        """Aumenta a velocidade do veículo em 10 unidades."""

        self.velocidade += 10
    
    def freiar(self):
        """Diminui a velocidade do veículo em 10 unidades."""

        self.velocidade -= 10

if __name__ == "__main__":
    Porsche_do_Gustavo = Carro("Porsche", "911", "2014")
    print(Porsche_do_Gustavo.marca, Porsche_do_Gustavo.modelo, Porsche_do_Gustavo.ano)
    Porsche_do_Gustavo.acelerar()
    Porsche_do_Gustavo.acelerar()
    Porsche_do_Gustavo.acelerar()
    Porsche_do_Gustavo.freiar()
    print(Porsche_do_Gustavo.velocidade)
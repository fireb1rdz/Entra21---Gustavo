"""
8) Crie uma classe chamada Veiculo com os seguintes atributos:
Marca (str)
Ano (int)
Valor base (float)
A classe deve ter um método abstrato chamado calcular_imposto() que calcula e retorna o valor do imposto a ser pago pelo veículo. 
O imposto é 2% do valor depreciado do veículo. A depreciação é calculada como 5% por ano desde o ano de fabricação do veículo até o ano atual em cima do valor base.
"""

class Veiculo:
    """Essa classe representa um veículo"""

    def __init__(self, marca: str, ano: int, valor_base: float) -> None:
        self.marca = marca
        self.ano = ano
        self.valor_base = valor_base

    def __str__(self) -> str:
        return f"Marca: {self.marca} | Ano: {self.ano} | Valor: {self.valor_base}"
    

    def calcular_imposto(self): 
        anos_considerados = 2023 - self.ano
        valor_depreciacao = anos_considerados * (5/100 * self.valor_base)
        valor_imposto = (2/100) * valor_depreciacao
        return valor_imposto

if __name__ == "__main__":
    meu_carro = Veiculo("Porsche", 2020, 100_000)
    print(meu_carro)
    print(meu_carro.calcular_imposto())
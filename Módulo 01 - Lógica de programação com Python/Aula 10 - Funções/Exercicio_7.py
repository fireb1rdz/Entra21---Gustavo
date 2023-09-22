"""
7. Defina uma função chamada "calcular_area" que recebe dois parâmetros: "base" e "altura".
Adicione anotações de função para indicar que os parâmetros são números e que a função retorna um número.
"""


def calcular_area(base: float, altura: float) -> float:
    return base * altura


print(f"A área é {calcular_area(float(input('Digite o valor da base: ')), float(input('Digite o valor da altura: ')))}")


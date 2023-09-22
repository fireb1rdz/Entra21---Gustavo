"""
2. Crie uma função chamada "dobro" que recebe um número como parâmetro e retorna o dobro desse número.
Inclua uma docstring que explique o propósito da função.
"""


def dobro(numero: int):
    """A função dobro solicita o input de um número como argumento, calcula e retorna o dobro dele."""
    print(f"O dobro de {numero} é {numero * 2}")


dobro(numero=int(input("Digite um número: ")))

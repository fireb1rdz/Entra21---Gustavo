"""
8. Crie uma função chamada "somar" que recebe uma quantidade variável de números como argumentos e retorna a soma deles.
"""


def somar(*args: int) -> int:
    """Retorna a soma dos argumentos"""
    return sum(args)


print(f"O resultado da soma é {somar(1,3,5,2)}")

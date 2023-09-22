"""
5. Escreva uma função chamada “repetir” que recebe dois parâmetros.
O primeiro é o elemento que repetirá, enquanto o segundo é o número de vezes que haverá a repetição.
Uma lista deve ser retornada.
"""

lista = []


def repetir(elemento, quantidade: int):
    for i in range(quantidade):
        lista.append(elemento)
    return lista


print(repetir("Teste", 5))

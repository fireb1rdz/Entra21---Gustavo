"""
14. Crie um algoritmo que receba duas listas como parâmetros
e retorne uma nova lista contendo os elementos intercalados das duas listas.
Por exemplo, se as listas forem `[1, 2, 3]` e `[4, 5, 6]`, o algoritmo deve retornar `[1, 2, 3, 4, 5, 6]`.
"""

lista1 = [int(input(f"Digite o {i + 1}º elemento: ")) for i in range(3)]
lista2 = [int(input(f"Digite o {i + 1}º elemento: ")) for i in range(3)]

lista_unificada = lista1 + lista2

print(f"O resultado é {lista_unificada}")

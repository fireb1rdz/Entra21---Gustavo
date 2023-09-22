"""
13. Escreva um programa que receba uma lista como entrada e remova todas as duplicatas,
retornando uma nova lista com os elementos únicos em sua ordem original.
"""

numeros = [int(input(f"Digite o {i + 1}º número: ")) for i in range(5)]

vetor_auxiliar = numeros.copy()
iguais = []

for indice, numero in enumerate(numeros):
    for indice2, numero2 in enumerate(vetor_auxiliar):
        if indice != indice2 and numero == numero2:
            iguais.append(vetor_auxiliar[indice])

for numero in iguais:
    if numero in vetor_auxiliar:
        vetor_auxiliar.remove(numero)


print(f"""
Lista de números: {numeros}
Lista de números únicos: {vetor_auxiliar}
""")
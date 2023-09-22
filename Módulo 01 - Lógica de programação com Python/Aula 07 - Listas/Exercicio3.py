"""
3. Escreva um programa que peça 5 números inteiros e armazene-os em uma lista.
Ao final, o programa deve mostrar o menor e o maior número da lista.
"""

maior = 0
menor = 0

numeros = [int(input(f"Digite o {numero + 1}º número: ")) for numero in range(5)]

for indice, numero in enumerate(numeros):
    if indice == 0:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numeros[indice]
    elif numero < menor:
        menor = numeros[indice]
print(f"""
Lista: {numeros}

Maior número da lista: {maior}

Menor número da lista: {menor}
""")
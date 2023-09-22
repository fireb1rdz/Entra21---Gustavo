"""
6. Crie um programa que receba uma lista de números e retorne a média dos números pares.
"""

numeros = [int(input(f"Digite o {i + 1}º número: ")) for i in range(5)]
numeros_pares = [numero for numero in numeros if numero % 2 == 0]

soma = 0

for numero in numeros:
    if numero % 2 == 0:
        soma += numero

print(f"""
A quantidade de números pares é {len(numeros_pares)}
A soma dos números pares é {soma}
A média dos números pares é {soma / len(numeros_pares):.2f}""")


"""
1. Escreva um programa que, dada uma lista de números, calcule a soma de todos os elementos.
"""

numeros = [int(input(f"Escolha 5 números, digite o {numero + 1}º número: ")) for numero in range(5)]
soma = 0

for numero in numeros:
    soma += numero
print(soma)
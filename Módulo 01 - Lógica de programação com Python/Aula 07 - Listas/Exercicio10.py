"""
10. Escreva um programa que receba uma lista de palavras e retorne a palavra mais longa.
"""

palavras = [input(f"Digite a {i + 1}ª palavra: ") for i in range(5)]

maior = palavras[0]
menor = palavras[0]

for letra in palavras:
    if len(letra) > len(maior):
        maior = letra
    elif len(letra) < len(menor):
        menor = letra
print(f"A maior palavra é {maior} e a menor palavra é {menor}")
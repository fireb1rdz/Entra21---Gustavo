"""
Escreva um programa que receba um número, se esse número for ímpar,
mostre na tela o quadrado do número digitado. No final do programa
mostre na tela a mensagem: “Programa finalizado…”.
"""

from math import sqrt
num = int(input("Digite um número: "))
if num % 2 == 1:
    print(f"{num} é ímpar, o quadrado de {num} é {sqrt(num):.2f}")
else:
    print(f"{num} é um número par")
print("Programa finalizado...")

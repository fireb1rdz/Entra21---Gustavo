"""
Escreva um programa que receba um número,
se esse número for par, mostre na tela
“O número é par” senão mostre “O número é ímpar”.
"""

num = int(input("Digite um numero: "))
if num % 2 == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")

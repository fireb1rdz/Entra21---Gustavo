"""
Escreva um programa que receba um número,
se esse número for par, mostre na tela a
metade do número digitado. No final do
programa mostre na tela a mensagem:
“Programa finalizado…”.
"""

num = int(input("Digite um número: "))
if num % 2 == 0:
    print(f"A metade de {num} é {num / 2}")
else:
    print(f"O número {num} não é par")
print("Programa finalizado...")

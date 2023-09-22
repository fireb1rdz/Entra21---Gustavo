"""
12. Escreva um programa que receba três valores: A, B e C.
Faça as comparações necessárias para exibir na tela o maior valor entre os três.
"""

valor_a = int(input("Digite o primeiro valor: "))
valor_b = int(input("Digite o segundo valor: "))
valor_c = int(input("Digite o terceiro valor: "))

if valor_c < valor_a > valor_b:
    print(f"O maior número é {valor_a}")
elif valor_a < valor_b > valor_c:
    print(f"O maior número é {valor_b}")
elif valor_a < valor_c > valor_b:
    print(f"O maior número é {valor_c}")
else:
    print(f"Os números são iguais.")


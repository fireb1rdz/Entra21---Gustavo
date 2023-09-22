"""
14. Escreva um programa que leia um número e informe se ele é divisível por 5.
"""

num = int(input("Digite um número: "))
if num % 5 == 0 and num != 0:
    print(f"O número {num} é divisível por 5.")
else:
    print(f"O número {num} não é divisível por 5")


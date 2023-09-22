"""
6. Escreva um programa que receba um número, se esse número estiver entre 20 e 90
mostre na tela a mensagem “O número está na faixa entre 20 e 90”,
se não, mostre “O número está fora da faixa”.
"""

num = int(input("Digite um número: "))
if 20 <= num <= 90:
    print(f"O número {num} está entre 20 e 90.")
else:
    print(f"O número {num} está fora da faixa entre 20 e 90.")

"""
21. Faça um programa que leia a idade de uma pessoa e exiba se ela é criança (até 12 anos),
adolescente (13 a 17 anos), adulto (18 a 59 anos) ou idoso (maiores de 60 anos).
"""

idade = int(input("Digite a sua idade: "))

while True:
    if idade <= 0:
        idade = int(input("Idade incorreta, digite novamente: "))
    else:
        break

if idade <= 12:
    print("Você é criança!")

elif idade <= 17:
    print("Você é adolescente!")

elif idade <= 59:
    print("Você é adulto(a)!")

else:
    print("Você é idoso(a)!")
"""
4. Crie um programa que receba o nome, idade, peso, altura e telefone do usuário
e mostre na tela as informações no seguinte formato:
Nome: <nome:
Idade: <idade>
Peso: <peso>
Altura: <altura>
Telefone: <telefone>
"""

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
telefone = input("Digite seu telefone: ")

print(f"Nome: {nome} \nIdade: {idade} \nPeso: {peso:.2f} \nAltura: {altura} \nTelefone: {telefone}")

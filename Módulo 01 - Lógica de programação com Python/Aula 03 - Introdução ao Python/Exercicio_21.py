"""
21. Escreva um programa que calcule o valor futuro de um investimento com base no montante inicial,
na taxa de juros e no período de tempo. Peça ao usuário para inserir essas informações e exiba o valor futuro.
Você pode utilizar a fórmula de juros compostos para realizar o cálculo.
"""

valor = float(input("Digite o valor do investimento: "))
juros = float(input("Digite a porcentagem de juros ao mês: "))
tempo = float(input("Digite a quantidade de meses: "))

resultado = valor * ((1 + (juros / 100)) ** tempo)

print(f"O valor final do investimento é: {resultado:,.2f}")
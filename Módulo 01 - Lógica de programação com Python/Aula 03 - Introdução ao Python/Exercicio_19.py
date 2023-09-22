"""
19. Faça um programa que leia o nome de um vendedor,
o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
informar o total a receber no final do mês, com duas casas decimais.
"""

nome = input("Digite o nome do vendedor: ")
salario = float(input("Digite um salario para o vendedor: "))
vendas = float(input("Digite um valor que o vendedor recebeu pelas vendas no mês: "))

comissao = vendas * 0.15
total = salario + comissao
print(f"O total a receber no final do mês será: {total:,.2f}")

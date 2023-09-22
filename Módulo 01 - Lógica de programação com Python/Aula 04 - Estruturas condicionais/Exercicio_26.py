"""
26. Crie um programa que auxilie no controle de gastos pessoais. Peça ao usuário para inserir suas despesas mensais nas seguintes categorias:
Alimentação
Moradia
Transporte
Lazer
Saúde
TV / Internet / Telefone
Também peça ao usuário o seu salário mensal.
O programa deve calcular o total de despesas,
mostrar o percentual de cada categoria em relação ao total e informar se as suas despesas excedem o salário.
"""

print("Insira suas despesas mensais nas seguintes categorias: ")

alimentacao = float(input("Alimentação: "))
moradia = float(input("Moradia: "))
transporte = float(input("Transporte: "))
lazer = float(input("Lazeres: "))
saude = float(input("Saúde: "))
tv_internet_telefone = float(input("TV / Internet / Telefone: "))

despesas = alimentacao + moradia + transporte + lazer + saude + tv_internet_telefone

salario = float(input("Digite seu salario mensal: "))

percentual1 = 100 * (alimentacao / despesas)
percentual2 = 100 * (moradia / despesas)
percentual3 = 100 * (transporte / despesas)
percentual4 = 100 * (lazer / despesas)
percentual5 = 100 * (saude / despesas)
percentual6 = 100 * (tv_internet_telefone / despesas)

print(f"""
O total de despesas foi R$ {despesas}

Alimentação: {percentual1:.2f}% 
Moradia: {percentual2:.2f}%
Transporte: {percentual3:.2f}%
Lazer: {percentual4:.2f}%
Saúde: {percentual5:.2f}%
TV, internet, telefone: {percentual6:.2f}%
""")

if despesas > salario:
    print("Suas despesas excedem seu salário!")
else:
    print("Suas despesas não excedem seu salário!")
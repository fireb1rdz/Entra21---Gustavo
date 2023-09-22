"""
7. Faça um programa que leia o salário de um trabalhador e o valor da prestação de um empréstimo.
Se a prestação for maior que 20% do salário imprima:
“empréstimo não concedido”, caso contrário imprima: “empréstimo concedido”.
"""

salario = float(input("Digite o seu salário: "))
percentual = salario * (20/100)

emprestimo = float(input("Digite o valor do empréstimo: "))

if emprestimo > percentual:
    print("Empréstimo não concedido!")
else:
    print("Empréstimo concedido!")
print(f"20% do seu salário é R$ {percentual} e o empréstimo é de R$ {emprestimo}")


"""
23. Faça um programa que leia um ano e verifique se ele é bissexto.
Um ano é bissexto se for divisível por 4, mas não divisível por 100, exceto se for divisível por 400.
"""

ano = int(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto!")
else:
    print(f"{ano} não é um ano bissexto!")


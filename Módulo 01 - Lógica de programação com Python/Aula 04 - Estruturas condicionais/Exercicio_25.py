"""
25. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero,
a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informa ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
import math

valor_a = int(input("Digite o valor de A: "))

if valor_a == 0:
    print("A equação não é do segundo grau")
else:
    valor_b = int(input("Digite o valor de B: "))
    valor_c = int(input("Digite o valor de C: "))

    delta = valor_b ** 2 - 4 * valor_a * valor_c

    if delta < 0:
        print("A equação não possui raízes reais")
    elif delta == 0:
        raiz = -valor_b / (2 * valor_a)
        print(f"A raiz real é {raiz}")
    else:
        raiz1 = -(-valor_b / math.sqrt(delta)) / (2 * valor_a)
        raiz2 = (-valor_b / math.sqrt(delta)) / (2 * valor_b)
        print(f"Raiz 1: {raiz1:.2f} \nRaiz 2: {raiz2:.2f}")

"""
20. Faça um programa que leia três números e exiba se eles formam um triângulo válido.
Um triângulo é válido se a soma de dois lados for maior que o terceiro lado.
"""

lado1 = float(input("Digite o valor do primeiro lado do triângulo: "))
lado2 = float(input("Digite o valor do segundo lado do triângulo: "))
lado3 = float(input("Digite o valor do terceiro lado do triângulo: "))

if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("O triângulo não é válido!")
else:
    print("O triângulo é valido!")
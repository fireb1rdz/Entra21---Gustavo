"""
13. Escreva um programa que leia as medidas dos lados de um triângulo e escreva
se ele é Equilátero, Isósceles ou Escaleno.

Sendo que:
Triângulo Equilátero: possui os 3 lados iguais.
Triângulo Isósceles: possui 2 lados iguais.
Triângulo Escaleno: possui 3 lados diferentes.
"""

lado1 = float(input("Digite a medida do primeiro lado: "))
lado2 = float(input("Digite a medida do segundo lado: "))
lado3 = float(input("Digite a medida do terceiro lado: "))

if lado1 == lado2 == lado3:
    print("Este é um triângulo equilátero!")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Este é um triângulo isósceles!")
else:
    print("Este é um triângulo escaleno!")

"""
16. Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio R.
A fórmula para calcular  volume é: (4/3) *  * R3.
"""

raio = float(input("Digite o valor do raio: "))
volume_esfera = (4 * 3.14 * raio ** 3)/3

print(f"O volume da esfera é {volume_esfera:.2f}")


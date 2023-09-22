"""
9. Faça um programa que receba três notas do usuário, calcule a média e mostre o resultado na tela.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

resultado = (nota1 + nota2 + nota3) / 3

print(f"A média das notas é {resultado:.2f}")

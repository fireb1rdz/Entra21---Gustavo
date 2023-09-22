"""
22. Faça um programa que leia a altura e o sexo (M ou F) de uma pessoa e calcule o peso ideal.
Para homens, o peso ideal é calculado pela fórmula: (72.7 * altura) - 58.
Para mulheres, o peso ideal é calculado pela fórmula: (62.1 * altura) - 44.7.
"""

altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo (M/F): ").lower()

while True:
    if altura <= 0 or sexo != "m" and sexo != "f":
        if altura <= 0:
            altura = float(input("Altura inválida, digite novamente:"))
        else:
            sexo = input("Sexo inválido, digite novamente (M/F): ")
    else:
        break

if sexo == "m":
    print(f"O seu peso ideal é {72.7 * altura - 58:.2f}")
else:
    print(f"O seu peso ideal é {62.1 * altura - 44.7:.2f}")

print("Programa encerrado!")

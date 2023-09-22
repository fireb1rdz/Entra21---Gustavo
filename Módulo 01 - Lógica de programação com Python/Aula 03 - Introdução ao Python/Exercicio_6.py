"""
6. Faça um algoritmo para calcular o IMC de uma pessoa com base no seu peso e altura.
"""

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
resultado = peso / (altura**2)
print(f"Seu IMC é: {resultado:.2f}")

if resultado < 17.3:
    print("Você está magro!")
elif resultado <= 25.5:
    print("Você está normal!")
elif resultado <= 29.7:
    print("Você está sobrepeso!")
else:
    print("Você está obeso!")


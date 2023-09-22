"""
7. Crie um programa que receba uma temperatura em graus Celsius e converta para Fahrenheit.
"""

temp = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (temp * 1.8) + 32

print(f"A temperatura {temp}°C convertida para Fahrenheit é {fahrenheit:.2f}°F")

maior = 0
menor = 0

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    if i == 0:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"""
O maior número da sequência foi: {maior}
O menor número da sequência foi: {menor}
""")

"""
3. Faça um programa para anonimizar o nome completo de uma pessoa ao substituir o último sobrenome com o caractere “#”.
"""

nome_completo = input("Digite seu nome completo: ").title().split()
ultimo_sobrenome = nome_completo[-1]

for letra in nome_completo[-1]:
    nome_completo[-1] = letra.replace(letra, "#")
print(f"O nome completo com sobrenome anonimatizado é {' '.join(nome_completo)}")



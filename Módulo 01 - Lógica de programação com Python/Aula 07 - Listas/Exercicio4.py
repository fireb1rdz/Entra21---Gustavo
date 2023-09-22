"""
4. Escreva um programa que receba duas listas
e retorne uma nova lista que contenha apenas os elementos em comum entre as duas listas.
"""

vetor1 = [int(input(f"Digite o {elemento + 1}º elemento da 1ª lista: ")) for elemento in range(5)]
vetor2 = [int(input(f"Digite o {elemento + 1}º elemento da 2ª lista: ")) for elemento in range(5)]

elementos_iguais = []

for elemento in vetor1:
    if elemento in vetor2:
        if not elemento in elementos_iguais:
            elementos_iguais.append(elemento)
print(f"""
Lista 1: {vetor1}
Lista 2: {vetor2}
Elementos iguais: {elementos_iguais}""")


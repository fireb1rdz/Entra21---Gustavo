"""
2. Escreva um programa que peça as três notas de um aluno armazenando-as em uma lista e retorne a média das notas.
"""

soma = 0
notas = [int(input(f"Digite a {nota + 1}ª nota: ")) for nota in range(5)]

for nota in notas:
    soma += nota
media = soma / len(notas)

print(f"A média do aluno é {media}")

"""
11. Faça um programa que receba uma lista de números inteiros e
retorne uma nova lista com os elementos em ordem crescente.
"""
numeros = [int(input(f"Digite o {i + 1}º número: ")) for i in range(5)]

fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim-1):
        if numeros[x] > numeros[x+1]:
            trocou = True
            temporario = numeros[x]
            numeros[x] = numeros[x+1]
            numeros[x+1] = temporario
        x += 1
    if not trocou:
        break
    fim -= 1
print(f"A lista em ordem crescente é {numeros}")
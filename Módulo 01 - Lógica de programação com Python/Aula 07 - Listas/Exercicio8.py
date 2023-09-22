"""
8. Faça um programa que leia um vetor de 8 posições e, em seguida,
leia também dois valores X e Y quaisquer correspondentes a duas posições no vetor. Ao final,
seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.
Se o usuário digitar valores inválidos para X ou Y mostre uma mensagem de erro
e peça novos valores até que ambos os valores sejam válidos.
"""

vetor = [int(input(f"Digite o {i + 1}º número: ")) for i in range(8)]

posicao1 = int(input("Digite a primeira posição: "))
posicao2 = int(input("Digite a segunda posição: "))

soma = 0

while posicao1 > 7 or posicao1 < 0:
    posicao1 = int(input("Digite um valor válido para a primeira posição: "))
while posicao2 > 7 or posicao2 < 0:
        posicao2 = int(input("Digite um valor válido para a segunda posição: "))

for indice, numero in enumerate(vetor):
    if indice == posicao1:
        soma += numero
    if indice == posicao2:
        soma += numero
print(f"""
Os números eram: {vetor}
A soma dos valores que estavam nas posições {posicao1, posicao2} resultou em: {soma}""")
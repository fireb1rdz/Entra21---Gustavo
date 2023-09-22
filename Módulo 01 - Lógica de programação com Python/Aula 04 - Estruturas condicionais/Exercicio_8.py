"""
8. Desenvolva um programa que recebe do usuário o placar de um jogo de futebol
(os gols de cada time) e informe se o resultado foi um empate,
a vitória do primeiro time ou do segundo time.
"""

placar1 = int(input("Quantos gols fez o primeiro time?: "))
placar2 = int(input("Quantos gols fez o segundo time?: "))

if placar1 > placar2:
    print(f"O primeiro time ganhou!")
elif placar1 < placar2:
    print("O segundo time ganhou!")
else:
    print("O jogo ficou empatado.")

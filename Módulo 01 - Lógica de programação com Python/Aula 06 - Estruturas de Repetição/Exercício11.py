import random
numero_aleatorio = random.randint(1, 100)
palpite = int(input("""
O computador está pensando em um número entre 1 e 100, tente adivinhar qual é!
Digite um número entre 1 e 100: """))

while palpite != numero_aleatorio:
    if palpite < numero_aleatorio:
        palpite = int(input(f"{palpite} é menor do que o número escolhido, tente novamente: "))
    elif palpite > numero_aleatorio:
        palpite = int(input(f"{palpite} é maior do que o número escolhido, tente novamente: "))

print(f"Você acertou!!! {palpite} era o número escolhido!!!! Parabéns!")


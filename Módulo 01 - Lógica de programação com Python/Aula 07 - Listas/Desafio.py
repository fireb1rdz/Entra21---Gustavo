def menu():
    continuar = 1
    while continuar:
        continuar = int(input("0. Sair \n" +
                              "1. Jogar novamente\n"))
        if continuar:
            game()
        else:
            print("Saindo...")


def game():
    jogada = 0

    while ganhou() == 0:
        print("\nJogador ", jogada % 2 + 1)
        exibe()
        linha = int(input("\nLinha :"))
        coluna = int(input("Coluna:"))

        if tabela[linha - 1][coluna - 1] == 0:
            if (jogada % 2 + 1) == 1:
                tabela[linha - 1][coluna - 1] = 1
            else:
                tabela[linha - 1][coluna - 1] = -1
        else:
            print("Nao esta vazio")
            jogada -= 1

        if jogada == 8:
            print("O jogo empatou!")
            break

        if ganhou():
            print("Jogador ", jogada % 2 + 1, " ganhou apos ", jogada + 1, " rodadas")

        jogada += 1


def ganhou():
    # checando linhas
    for i in range(3):
        soma = tabela[i][0] + tabela[i][1] + tabela[i][2]
        if soma == 3 or soma == -3:
            return 1

    # checando colunas
    for i in range(3):
        soma = tabela[0][i] + tabela[1][i] + tabela[2][i]
        if soma == 3 or soma == -3:
            return 1

    # checando diagonais
    diagonal1 = tabela[0][0] + tabela[1][1] + tabela[2][2]
    diagonal2 = tabela[0][2] + tabela[1][1] + tabela[2][0]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1

    return 0


def exibe():
    for i in range(3):
        for j in range(3):
            if tabela[i][j] == 0:
                print(" _ ", end=' ')
            elif tabela[i][j] == 1:
                print(" X ", end=' ')
            elif tabela[i][j] == -1:
                print(" O ", end=' ')

        print()


tabela = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

menu()
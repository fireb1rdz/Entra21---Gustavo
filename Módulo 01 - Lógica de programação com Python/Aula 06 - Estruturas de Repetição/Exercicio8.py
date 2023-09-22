"""
8. Um restaurante de fast-food oferece um menu com 4 opções de hambúrgueres:
X-Burger, X-Salada, X-Bacon e X-Tudo.
Cada hambúrguer tem um preço diferente: R$10, R$12, R$15 e R$18, respectivamente.
Escreva um programa que solicite ao usuário a quantidade desejada de cada hambúrguer e exiba o valor total do pedido.
"""

# Variáveis de quantidade

quantidade_x_burguer = 0
quantidade_x_salada = 0
quantidade_x_bacon = 0
quantidade_x_tudo = 0

# Constantes de valor

PRECO_X_BURGUER = 10
PRECO_X_SALADA = 12
PRECO_X_BACON = 15
PRECO_X_TUDO = 18

# Valor do pedido

valor_total = 0


while True:
    opcao = str(input("""
Bem vindo ao Fast-Food!

Aqui estão nossas opções:

1) X - Burguer
2) X - Salada
3) X - Bacon
4) X - Tudo
0) Finalizar pedido

Digite a opção desejada: """))

    match opcao:
        case "1":
            quantidade_x_burguer += int(input("Digite a quantidade de X - Burguers: "))
            valor_total += quantidade_x_burguer * PRECO_X_BURGUER

        case "2":
            quantidade_x_salada += int(input("Digite a quantidade de X - Saladas: "))
            valor_total += quantidade_x_salada * PRECO_X_SALADA

        case "3":
            quantidade_x_bacon += int(input("Digite a quantidade de X - Bacons: "))
            valor_total += quantidade_x_bacon * PRECO_X_BACON

        case "4":
            quantidade_x_tudo += int(input("Digite a quantidade de X - Tudo: "))
            valor_total += quantidade_x_tudo * PRECO_X_TUDO

        case "0":
            break
        case _:
            print("Dígito incorreto!")
            continue

print(f"""
Quantidade de X - Burguers: {quantidade_x_burguer}
Quantidade de X - Saladas: {quantidade_x_salada}
Quantidade de X - Bacons: {quantidade_x_bacon}
Quantidade de X - Tudo: {quantidade_x_tudo}

Valor total do pedido: R$ {valor_total:.2f}
""")
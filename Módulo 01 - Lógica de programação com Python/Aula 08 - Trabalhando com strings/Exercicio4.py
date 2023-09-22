"""
4. Faça um programa que abrevie o nome fornecido pelo usuário de acordo com os exemplos fornecidos:

João Carlos Nascimento -> João C. Nascimento
Marcos Andrade Costa Júnior -> Marcos A. C. Júnior
Ana Maria -> AM
"""

nomes = input("Digite seu nome completo: ").title().split()
nome_abreviado = ""
letra_inicial = 0

if len(nomes) < 3:
    nome_abreviado = ""
    for nome in nomes:
        nome_abreviado += nome[0]
    print(f"Seu nome abreviado é {nome_abreviado}")

else:
    for indice, nome in enumerate(nomes[1: -1]):
        for indice2, letra in enumerate(nome):
            if indice2 == 0:
                letra_inicial = letra
                nomes[indice + 1] = nome.replace(nome, letra_inicial + ".")
                letra_inicial = ""

    nomes_abreviado = " ".join(nomes)
    print(f"Seu nome abreviado é: {nomes_abreviado}")

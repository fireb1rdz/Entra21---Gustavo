"""
6. Escreva um algoritmo que solicita ao usuário um texto e o limite de caracteres do texto.
Se o texto exceder o limite de caracteres o algoritmo deve
retornar o texto com o final da string contendo os caracteres: “...”.
"""

texto = input("Digite um texto: ")
limite_caracteres = int(input("Digite o limite de caracteres: "))



if len(texto) > limite_caracteres:
    print(texto[:limite_caracteres - 3] + "...")
else:
    print(texto)
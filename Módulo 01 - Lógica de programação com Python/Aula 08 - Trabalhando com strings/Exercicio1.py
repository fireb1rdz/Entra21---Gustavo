"""
1. Faça um programa que então leia uma string e a imprima.
Caso o valor digitado não seja um valor textual (ex.: 12345),
uma mensagem deve ser mostrada para o usuário
e o valor deve continuar sendo solicitado até que o mesmo seja válido.
"""

texto = input("Digite um texto: ")

texto_formatado = texto.replace(" ", "")

while True:
    if texto_formatado.isalpha():
        print(f"O texto ({texto}) é válido.")
        break
    else:
        texto = input("Digite um texto válido: ")
        texto_formatado = texto.replace(" ", "")
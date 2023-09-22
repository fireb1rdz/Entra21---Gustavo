"""
10. Escreva um algoritmo que retorne o número de palavras únicas em um texto.
Ignore a diferenciação entre maiúsculas e minúsculas.
"""

texto = input("Digite um texto: ").lower()
palavras = texto.split()
palavras_unicas = []
resultado = 0

for palavra in palavras:
    if not palavra in palavras_unicas:
        resultado += 1
        palavras_unicas.append(palavra)
    else:
        resultado -= 1

print(f"A quantidade de palavras únicas é {resultado}")

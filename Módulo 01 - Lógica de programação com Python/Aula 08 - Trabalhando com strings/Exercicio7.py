"""
7. Escreva um algoritmo que encontre todas as ocorrências de números em uma string e os retorne em uma lista.
"""

import re

padrao = r"\d"

texto = input("Digite um texto: ")

numeros_texto = re.search(padrao, texto)

if numeros_texto:
    numeros = re.findall(padrao, texto)
    print(f"""
Os números encontrados no texto inserido são: {", ".join(numeros)}""")

else:
    print("Não foram encontrados números no texto inserido.")
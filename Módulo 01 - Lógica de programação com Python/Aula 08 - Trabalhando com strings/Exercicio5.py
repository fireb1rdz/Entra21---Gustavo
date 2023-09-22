"""
5. Escreva um algoritmo que chega se o texto de uma string é spam.
Para ser considerado spam a string deve conter as palavras “jequiti” ou “curso de python”.
"""

import re
padrao = r"jequiti|curso\s?de\s?python"

texto = input("Digite um texto: ")

spam = re.search(padrao, texto)

if spam:
    print(f"O texto digitado é um spam!")
else:
    print(f"O texto digitado não é spam!")

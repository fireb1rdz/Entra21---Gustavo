"""
9. Escreva um programa que solicite ao usuário um texto e uma tag HTML.
Após isso, encapsule a string com essa tag. Exemplo: texto = “Olá”, tag = “b”. Deve retornar <b>Olá</b>.
"""

texto = input("Digite um texto: ")
tag = input("Digite uma tag: ")

print(f"<{tag}>{texto}</{tag}>")

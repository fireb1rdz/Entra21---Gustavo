"""
8. Construa um programa que receba um texto e uma palavra como entrada e indique se a
palavra está presente ou não no texto. Se a palavra estiver presente no texto, diga quantas vezes ela aparece.
"""
texto = input("Digite um texto: ").split()
palavra = input("Digite uma palavra: ")

if palavra in texto:
    quantidade_vezes = texto.count(palavra)
    print(f"A palavra {palavra} aparece {quantidade_vezes} vez(es) no texto")
if not palavra in texto:
    print(f"A palavra {palavra} não aparece no texto.")
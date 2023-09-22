"""
13. Crie um programa que solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.
"""

numero = int(input("Digite um número: "))
for contador in range(0,11):
    print(f"{numero} * {contador} = {numero*contador}")



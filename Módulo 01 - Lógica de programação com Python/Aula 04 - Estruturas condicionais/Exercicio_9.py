"""
9. Escreva um programa que leia um inteiro entre 1 e 7
e imprima o dia da semana correspondente a este número.
Isto é, domingo se for 1, segunda-feira se for 2, e assim por diante.
"""

dia = int(input("Digite um número entre 1 e 7: "))
match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sábado")
    case _:
        print("Dia inválido")

"""
18. Faça um algoritmo que simule uma calculadora.
Para isso, o algoritmo deverá solicitar dois números e a operação matemática que deve ser executada.
O algoritmo deve permitir as operações de adição, subtração, multiplicação e divisão.
"""

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

operacao = int(input(""" 
1) Adição
2) Subratração
3) Multiplicação
4) Divisão

Digite o número correspondente à operação desejada:
"""))

match operacao:
    case 1:
        print(f"{valor1} + {valor2} = {valor1 + valor2}")
    case 2:
        print(f"{valor1} - {valor2} = {valor1 - valor2}")
    case 3:
        print(f"{valor1} * {valor2} = {valor1 * valor2}")
    case 4:
        print(f"{valor1} / {valor2} = {valor1 / valor2:.2f}")
    case _:
        print(f"Operação inválida!")

print("Programa encerrado!")
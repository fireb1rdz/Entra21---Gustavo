dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
dividendo_inicial = dividendo

quoeficiente = 0
i = 0

while dividendo > 0:
    if dividendo > 0:
        dividendo -= divisor
        quoeficiente += 1
        i += 1
print(f"O resultado da divisão entre {dividendo_inicial} e {divisor} é {quoeficiente}")
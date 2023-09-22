valor_inicial = int(input("Digite o valor inicial do intervalo de números: "))
valor_final = int(input("Digite o valor final do intervalo de números: "))

for i in range(valor_inicial, valor_final + 1):
    if i % 2 == 0:
        print(i)
else:
    print("Não há números pares neste intervalo!")

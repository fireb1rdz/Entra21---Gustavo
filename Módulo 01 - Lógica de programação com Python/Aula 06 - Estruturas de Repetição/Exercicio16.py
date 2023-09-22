numero = int(input("Digite um número: "))

for i in range(numero + 1, 0, -1):
    if numero % i == 0:
        print(f"{numero} é divisível por {i}!")

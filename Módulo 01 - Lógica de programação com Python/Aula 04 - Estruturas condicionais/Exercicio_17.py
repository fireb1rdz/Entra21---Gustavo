numero = int(input("Digite um número de 3 dígitos: "))
if numero > 0:
    digito1 = numero % 10
    digito2 = numero // 10 % 10
    digito3 = numero // 100 % 10

    numero_invertido = digito1 * 1000 + digito2 * 100 + digito3 * 10

    print(f"O número inverso de {numero} é {numero_invertido}")
else:
    print(f"O valor inverso de {numero} é {resultado}.")



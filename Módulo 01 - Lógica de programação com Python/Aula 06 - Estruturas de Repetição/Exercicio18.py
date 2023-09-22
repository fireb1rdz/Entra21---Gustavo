palavra = input("Digite uma palavra: ")

for i in range(len(palavra)):
    if palavra[i] != palavra[-i-1]:
        print(f"{palavra} não é um palíndromo!")
        break
else:
    print(f"{palavra} é um palíndromo! ")




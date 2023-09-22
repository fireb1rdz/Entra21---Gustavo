"""3. Implemente um algoritmo que declare uma lista de strings
e retorne uma tupla contendo a quantidade de palavras em cada string."""

strings = [input("Digite uma frase: ") for string in range(3)]
contador_palavras = 0
quantidade_palavras = []

for palavras in strings:
    contador_palavras = len(palavras.split())
    quantidade_palavras.append(contador_palavras)

tupla = tuple(quantidade_palavras)

print(f"A quantidade de palavras em cada string é {tupla}")
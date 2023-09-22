"""8. Crie um algoritmo que mapeie palavras em inglês para a sua tradução em um dicionário,
após isso peça para o usuário digitar um texto em inglês com as palavras contidas no
dicionário e mostre o texto traduzido."""

dicionario = {
   "hello": "olá",
   "world": "mundo",
   "good": "bom",
   "morning": "manhã"
}


texto_ingles = input("Digite um texto em inglês: ")


palavras = texto_ingles.split()


traducoes = []


for palavra in palavras:
   traducao = dicionario.get(palavra.lower(), palavra)
   traducoes.append(traducao)


texto_traduzido = " ".join(traducoes)


print("Texto traduzido:")
print(texto_traduzido)
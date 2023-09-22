"""
9. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor .
Depois, mostre quantas vezes cada valor foi conseguido.
Dica: use um vetor de contadores(1-6) e uma função para gerar números aleatórios, simulando os lançamentos dos dados.
"""

import random
resultados = [int(random.randint(1, 6)) for numero in range(100)]

valor1 = 0
valor2 = 0
valor3 = 0
valor4 = 0
valor5 = 0
valor6 = 0

for numero in resultados:
    if numero == 1:
        valor1 += 1
    if numero == 2:
        valor2 += 1
    if numero == 3:
        valor3 += 1
    if numero == 4:
        valor4 += 1
    if numero == 5:
        valor5 += 1
    if numero == 6:
        valor6 += 1

print(f"""
Quantidade de vezes em que caiu 1: {valor1}
Quantidade de vezes em que caiu 2: {valor2}
Quantidade de vezes em que caiu 3: {valor3}
Quantidade de vezes em que caiu 4: {valor4}
Quantidade de vezes em que caiu 5: {valor5}
Quantidade de vezes em que caiu 6: {valor6}
""")
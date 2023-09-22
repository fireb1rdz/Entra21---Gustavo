"""
15. Escreva um programa que receba uma lista como entrada e retorne uma nova lista comprimida,
onde elementos repetidos sejam substituídos por uma tupla contendo o elemento e a quantidade de vezes que ele se repete.
Por exemplo, para a lista [1, 1, 1, 2, 3, 3, 4, 4, 4, 4], o programa deve retornar [(1, 3), 2, (3, 2), (4, 4)].
"""

lista_entrada = input("Digite uma lista de elementos separados por espaço: ").split()
lista_comprimida = []

elemento_atual = None
contagem_atual = 0

for elemento in lista_entrada:
    if elemento == elemento_atual:
        contagem_atual += 1
    else:
        if elemento_atual is not None:
            if contagem_atual > 1:
                lista_comprimida.append((elemento_atual, contagem_atual))
            else:
                lista_comprimida.append(elemento_atual)
        elemento_atual = elemento
        contagem_atual = 1
if contagem_atual > 1:
    lista_comprimida.append((elemento_atual, contagem_atual))
else:
    lista_comprimida.append(elemento_atual)

print(lista_comprimida)
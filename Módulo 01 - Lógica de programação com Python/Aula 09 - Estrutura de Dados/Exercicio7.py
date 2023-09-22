"""7. Escreva um programa que leia os valores de uma matriz 3x3 e um valor X. O programa deverá fazer uma busca
na matriz e, ao final, mostrar a localização (linha e coluna) do valor X. Caso o valor X não esteja
presente na matriz o programa deve mostrar a mensagem “Não encontrado”."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for i in range(3):
   for j in range(3):
       matriz[i][j] = int(input(f"Digite o valor da posição ({i+1}, {j+1}): "))


valor_x = int(input("Digite o valor X a ser procurado: "))


encontrado = False
linha_x, coluna_x = None, None


for i in range(3):
   for j in range(3):
       if matriz[i][j] == valor_x:
           encontrado = True
           linha_x, coluna_x = i, j
           break


if encontrado:
   print(f"O valor {valor_x} foi encontrado na posição ({linha_x + 1}, {coluna_x + 1}).")
else:
   print("Não encontrado.")
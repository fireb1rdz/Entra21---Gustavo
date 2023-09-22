"""5. Escreva um programa que leia os valores de uma matriz 3x3,
conte e mostre quantos valores maiores que 10 ela possui."""

matriz = [[6, 8, 11], [14, 25, 6], [7, 8, 9]]
contagem = 0


for i in range(3):
   for j in range(3):
       if matriz[i][j] > 10:
           contagem += 1


print("Matriz:")
for linha in matriz:
   print(linha)


print(f"Quantidade de valores maiores que 10 na matriz: {contagem}")
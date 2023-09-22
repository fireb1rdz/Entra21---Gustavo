"""6. Escreva um programa que solicite o tamanho de uma matriz identidade e mostre ela na tela."""

tamanho = int(input("Digite o tamanho da matriz identidade: "))

matriz_identidade = []
for i in range(tamanho):
   linha = []
   for j in range(tamanho):
       if i == j:
           linha.append(1)
       else:
           linha.append(0)
   matriz_identidade.append(linha)


print("Matriz Identidade:")
for linha in matriz_identidade:
   print(linha)
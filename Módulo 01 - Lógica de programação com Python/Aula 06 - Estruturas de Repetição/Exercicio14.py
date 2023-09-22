x = int(input("Digite o valor de x: "))
n = int(input("Digite o valor de n: "))

soma = 1

for i in range(1, n + 1):
    soma *= x
print(soma)
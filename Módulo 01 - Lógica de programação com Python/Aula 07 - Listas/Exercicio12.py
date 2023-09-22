"""
12. Dada uma lista de números inteiros, escreva um programa que encontre a soma dos números consecutivos maiores
do que zero. Por exemplo, para a lista [ -2, 3, 4, 0, 7, -1], o programa deve retornar a soma 7 (3 + 4).
"""

numeros = [int(input(f"Digite o {i + 1}º número: ")) for i in range(5)]

numeros_soma = []
resultado_soma = 0
numero_consecutivo = False
x = 0
fim = 5
soma = 0

while x <= (fim - 1):
    if numeros[x] > 0:
        if not numeros[x] in numeros_soma:
            if numeros[x - 1] in numeros_soma and numeros[x - 1] == numeros[x] - 1:
                numeros_soma.append(numeros[x])
            else:
                if numeros[x] - 1 == numeros[x - 1]:
                    numero_consecutivo = True
                else:
                    numero_consecutivo = False
                if numero_consecutivo == True:
                    numeros_soma.append(numeros[x - 1])
                    numeros_soma.append(numeros[x])
    x += 1

for i in numeros_soma:
    soma += i

resultado_soma = soma

print(f"""Os números consecutivos são {numeros_soma} e o resultado da soma deles é {resultado_soma}""")


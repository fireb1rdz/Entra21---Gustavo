fator1 = int(input("Digite o primeiro fator: "))
fator2 = int(input("Digite o segundo fator: "))

resultado = 0

for i in range(0, fator2):
    if i < fator2:
        resultado += fator1
print(f"O resultado da multiplicação de {fator1} e {fator2} é {resultado}")
parar = False
soma = 0

print("\nCaso deseje encerrar o programa, digite 0")
while not parar:
    numero_digitado = int(input(f"""
A soma dos números digitados até o momento é {soma}
Digite um numero inteiro positivo: """))
    soma += numero_digitado
    if numero_digitado <= 0:
        break
print(f"Programa encerrado! a soma total foi {soma}")

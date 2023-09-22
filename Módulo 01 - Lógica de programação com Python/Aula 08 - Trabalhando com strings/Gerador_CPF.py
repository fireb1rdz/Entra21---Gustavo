"""
Utilizando partes do código de validação do CPF e o pacote random, construa um gerador de cpfs.
"""
import time
import random

digito_verificador_1 = 0
digito_verificador_2 = 0
cpf_gerado = []
cpf_gerado_string = []


while True:
    start = input("""
Bem vindo ao gerador de CPF! 

Deseja iniciar o programa agora? [s/n]: 
""").lower()
    while not start == "s":
        start = input("""
Deseja iniciar o programa agora? [s/n]: 
""")
    else:
        break

print("""
Aguarde enquanto seu CPF está sendo gerado...""")

time.sleep(2)

# Gerar CPF

for digito in range(0, 11):
    cpf_gerado.append(random.randint(0,9))


# Inserir CPF em lista de string

for digito in cpf_gerado:
    cpf_gerado_string.append(str(digito))


# Multiplicação para verificar 1 dígito conforme tabela

soma = 0
multiplicador = 1

for digito in cpf_gerado[8::-1]:
    multiplicador += 1
    soma += digito * multiplicador


# Divisão por 11, considerando quociente apenas o valor inteiro

resto_divisao = soma % 11


# Condicional para verificar o primeiro dígito

if resto_divisao >= 2:
    digito_verificador_1 = 11 - resto_divisao


# Armazenar CPF com primeiro digito correto

cpf_correto = cpf_gerado.copy()

for indice, digito in enumerate(cpf_correto):
    if indice == 9:
        cpf_correto[indice] = digito_verificador_1


# Multiplicação para verificar 2 dígito conforme tabela

soma = 0
multiplicador = 1

for digito in cpf_correto[9::-1]:
    multiplicador += 1
    soma += digito * multiplicador


# Divisão por 11, considerando quociente apenas o valor inteiro

resto_divisao = soma % 11

# Condicional para verificar o segundo dígito

if resto_divisao >= 2:
    digito_verificador_2 = 11 - resto_divisao


# Armazenar CPF com segundo dígito correto

for indice, digito in enumerate(cpf_correto):
    if indice == 10:
        cpf_correto[indice] = digito_verificador_2


# Transformando variável cpf_correto em string

cpf_correto_string = []
for digito in cpf_correto:
    cpf_correto_string.append(str(digito))


# Apresentando o CPF gerado

print(f"""
CPF gerado: {"".join(cpf_correto_string[0:3])}.{"".join(cpf_correto_string[3:6])}.{"".join(cpf_correto_string[6:9])}-{"".join(cpf_correto_string[9:])}
""")

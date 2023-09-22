"""
18. Refaça a questão anterior validando se o cpf é válido através do dígito verificador.
O algoritmo para fazer essa validação está descrito aqui:
https://www.macoratti.net/alg_cpf.htm#:~:text=O%20algoritmo%20de%20valida%C3%A7%C3%A3o%20do,%3A%20111.444.777%2D05.
"""

import copy
import re

# Receber o CPF e criação das variáveis de dígito verificador e cpf correto

cpf = input("Digite o seu CPF: ")
digito_verificador_1 = 0
digito_verificador_2 = 0
cpf_correto = []


# Padrão para localizar apenas dígitos do CPF

padrao = r"\d"


# Verificar se entrada está de acordo com padrão

verificar_entrada = re.match(padrao, cpf)


# Se entrada não estiver de acordo com padrão ou tiver mais ou menos dígitos que o necessário, solicita novo valor

while True:
    if not verificar_entrada or len(re.findall(padrao, cpf)) < 11 or len(re.findall(padrao, cpf)) > 11:
        cpf = input("Digite um cpf válido: ")
        verificar_entrada = re.match(padrao, cpf)
    else:
        break


# Adiciona o CPF formatado em valor do tipo inteiro em uma lista

cpf_string = re.findall(padrao,cpf)
cpf_formatado = []
for digito in cpf_string:
    cpf_formatado.append(int(digito))


# Multiplicação para verificar 1 dígito conforme tabela

soma = 0
multiplicador = 1

for digito in cpf_formatado[8::-1]:
    multiplicador += 1
    soma += digito * multiplicador


# Divisão por 11, considerando quociente apenas o valor inteiro

resto_divisao = soma % 11


# Condicional para verificar o primeiro dígito

if resto_divisao >= 2:
    digito_verificador_1 = 11 - resto_divisao


# Armazenar CPF com primeiro digito correto

cpf_correto = cpf_formatado.copy()

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


# Comparação entre o CPF correto e o informado pelo usuário

if cpf_formatado == cpf_correto:
    print("O CPF informado é válido!")
else:
    print(f"""
O CPF informado é inválido!

CPF informado: {"".join(cpf_string[0:3])}.{"".join(cpf_string[3:6])}.{"".join(cpf_string[6:9])}-{"".join(cpf_string[9:])}
CPF correto:   {"".join(cpf_correto_string[0:3])}.{"".join(cpf_correto_string[3:6])}.{"".join(cpf_correto_string[6:9])}-{"".join(cpf_correto_string[9:])}
""")
"""
10. Escreva uma função “formata_cpf” que recebe um número inteiro e converta ele para uma string no
formato do cpf “000.000.000-00”. Caso o número fornecido não seja válido a função
deve retornar o próprio número em formato de string.
"""
import re


def formata_cpf(cpf):

    # Receber o CPF e criação das variáveis de dígito verificador e cpf correto

    digito_verificador_1 = 0
    digito_verificador_2 = 0
    cpf_correto = []

    # Padrão para localizar apenas dígitos do CPF

    padrao = r"\d"

    # Verificar se entrada está de acordo com padrão

    if not re.match(padrao, cpf):
        return cpf

    # Adiciona o CPF formatado em valor do tipo inteiro em uma lista

    cpf_string = re.findall(padrao, cpf)
    cpf_formatado = []
    for digito in cpf_string:
        cpf_formatado.append(int(digito))

    # Multiplicação para verificar 1 dígito conforme tabela

    soma = 0
    multiplicador = 1

    for digito in cpf_formatado[8::-1]:
        multiplicador += 1
        soma += digito * multiplicador

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

    if cpf_formatado != cpf_correto:
        return cpf
    return f"{''.join(cpf_string[0:3])}.{''.join(cpf_string[3:6])}.{''.join(cpf_string[6:9])}-{''.join(cpf_string[9:])}"

print(formata_cpf("80683544250"))
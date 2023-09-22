"""
9. Escreva uma função chamada "mostrar_informacoes" que recebe um número variável de
argumentos nomeados e imprime cada argumento no formato "chave: valor". Por exemplo: "nome: João", "idade: 25".
"""


def mostrar_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


mostrar_informacoes(nome="Joao", idade=25, cidade="Doutor Pedrinho")


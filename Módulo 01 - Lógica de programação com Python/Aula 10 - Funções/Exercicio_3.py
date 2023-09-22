"""
3. Crie uma função chamada "apresentacao" que recebe o nome de uma pessoa como parâmetro
e imprime uma saudação personalizada. Se nenhum nome for fornecido, a saudação deve ser genérica como "Olá, amigo!".
"""


def apresentacao(nome="amigo!"):
    print(f"Olá, {nome}!")


apresentacao("Pedro")

"""
18. Construa um algoritmo que leia o preço de um produto, o percentual de desconto
e calcule o valor a pagar e o valor do desconto.
"""

preco = float(input("Digite o preço: "))
percentual_desconto = int(input("Digite o percentual do desconto: "))
valor_desconto = (preco *(percentual_desconto / 100))
valor_pagar = preco - valor_desconto

print(f"O valor do produto é {preco}, com {percentual_desconto}% de desconto. O preço à pagar é {valor_pagar} e o valor do desconto é {valor_desconto}")

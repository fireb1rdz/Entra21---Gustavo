"""
5. Dada uma lista de nomes, crie uma nova lista que contenha apenas os nomes que começam com a letra “A”.
"""

nomes = [input(f"Digite o {i + 1} nome: ").capitalize() for i in range(5)]

nomes_com_a = [nome for nome in nomes if nome[0] == "A"]
print(f"Os nomes que começam com a letra A são: {nomes_com_a}")

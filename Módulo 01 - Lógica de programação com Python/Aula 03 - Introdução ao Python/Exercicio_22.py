"""
22. Faça um programa que leia o nome de um livro, o tempo médio (em segundos)
que o usuário leva para ler uma página do livro, o tempo de leitura diário
(em segundos) e a quantidade de páginas de um livro.
Ao final, o programa deverá mostrar um relatório que mostre:

Quantidade de páginas lidas por dia
Quantidade de horas necessárias para ler o livro
Quantidade de dias necessários para ler o livro
Quantidade de semanas necessárias para ler o livro
"""

nome = input("Digite o nome do livro: ")
tempo_pagina = int(input("Digite o tempo em segundos para leitura de uma pagina: "))
tempo_dia = int(input("Digite o tempo diário de leitura em segundos: "))
quantidade_paginas = int(input("Digite a quantidade de paginas do livro: "))


quantidade_paginas_dia = tempo_dia / tempo_pagina
horas_dia = tempo_dia / 3600
quantidade_horas_livro = ((quantidade_paginas * tempo_pagina) / 3600)
quantidade_dias_livro = quantidade_paginas / quantidade_paginas_dia
quantidade_semanas_livro = quantidade_dias_livro / 7


print(f"A quantidade de paginas lidas por dia é {quantidade_paginas_dia}")
print(f"A quantidade de horas necessárias para finalizar o livro é {quantidade_horas_livro}")
print(f"A quantidade de dias necessários para finalizar o livro é {quantidade_dias_livro}")
print(f"A quantidade de semanas necessárias para finalizar o livro é {quantidade_semanas_livro}")

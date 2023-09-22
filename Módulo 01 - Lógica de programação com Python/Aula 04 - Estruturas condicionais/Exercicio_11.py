"""
11. Faça um programa que pergunte em que turno você estuda.
Peça para digitar M - Matutino, V - Vespertino ou N - Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!"
ou "Valor Inválido!" de acordo com o turno escolhido.
"""

turno = input("""Em qual turno você estuda?
 M - Matutino
 V - Vespertino
 N - Noturno
 
 Digite a opção desejada: """).upper()

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")

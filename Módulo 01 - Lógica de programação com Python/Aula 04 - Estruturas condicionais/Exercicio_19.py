"""
19. Faça um algoritmo que calcule o peso de uma pessoa em outros planetas.
Para isso o programa deve solicitar o peso da pessoa,
em qual planeta ela deseja saber o seu peso e utilizar a seguinte escala de gravidade dos planetas em relação a terra:

Mercúrio: 0.38
Vênus: 0.91
Marte: 0.38
Júpiter: 2.34
Saturno: 0.93
Urano: 0.92
Netuno: 1.12
Plutão: 0.06
"""
peso = float(input("Digite seu peso em quilogramas: "))

while True:
    if peso <= 0:
        peso = float(input("Peso incorreto, digite novamente: "))
    else:
        break

planeta = int(input("""
1) Mercúrio
2) Vênus
3) Marte
4) Júpiter
5) Saturno
6) Urano
7) Netuno
8) Plutão

Digite o planeta no qual você deseja saber seu peso, de acordo com a tabela acima: 
"""))

match planeta:
    case 1:
        print(f"Seu peso em Mercúrio é {peso * 0.38:.2f} kg")
    case 2:
        print(f"Seu peso em Vênus é {peso * 0.91:.2f} kg")
    case 3:
        print(f"Seu peso em Marte é {peso * 0.38:.2f} kg")
    case 4:
        print(f"Seu peso em Júpiter é {peso * 2.34:.2f} kg")
    case 5:
        print(f"Seu peso em Saturno é {peso * 0.93:.2f} kg")
    case 6:
        print(f"Seu peso em Urano é {peso * 0.92:.2f} kg")
    case 7:
        print(f"Seu peso em Netuno é {peso * 1.12:.2f} kg")
    case 8:
        print(f"Seu peso em Plutão é {peso * 0.06:.2f} kg")
    case _:
        print("Planeta inválido!")
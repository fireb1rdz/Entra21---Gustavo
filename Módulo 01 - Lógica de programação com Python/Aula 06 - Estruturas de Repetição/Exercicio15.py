soma_total = 0
quantidade_notas_total = 0

for i in range(5):
    media = 0
    for j in range(3):
        nota = int(input(f"Digite a {j + 1}ª nota: "))
        media += nota
        quantidade_notas_total += 1
        soma_total += nota
    media = media / 3
    print(f"A média do {i + 1}º aluno é {media:.2f}")

media_turma = soma_total / quantidade_notas_total
print(f"A média da turma é {media_turma}")

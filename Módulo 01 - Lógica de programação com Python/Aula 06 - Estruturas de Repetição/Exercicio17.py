nome = input("Digite o seu nome: ")
vogal = 0
consoante = 0

for l in nome:
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        vogal += 1
    else:
        consoante += 1
print(f"{nome} tem {vogal} vogal (is) e {consoante} consoante(s)")

degraus = int(input("Digite a quantidade de degraus: "))

for i in range(degraus + 1):
    print(" " * degraus, end="")
    print("#" * i)
    degraus -= 1


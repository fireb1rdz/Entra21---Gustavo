"""10. Crie um algoritmo que leia o nome, cpf e idade de várias pessoas e salve essas informações
em uma lista de dicionários. No final o programa deverá mostrar uma lista com os dados das pessoas classificadas
em: pessoas maiores de idade e pessoas menores de idade."""

pessoas = []


while True:
   nome = input("Digite o nome da pessoa (ou Enter para encerrar): ")
   if not nome:
       break
   cpf = input("Digite o CPF da pessoa: ")
   idade = int(input("Digite a idade da pessoa: "))


   pessoa = {"nome": nome, "cpf": cpf, "idade": idade}
   pessoas.append(pessoa)


maiores_de_idade = []
menores_de_idade = []


for pessoa in pessoas:
   if pessoa["idade"] >= 18:
       maiores_de_idade.append(pessoa)
   else:
       menores_de_idade.append(pessoa)


print("Pessoas Maiores de Idade:")
for pessoa in maiores_de_idade:
   print(f"Nome: {pessoa['nome']}, CPF: {pessoa['cpf']}, Idade: {pessoa['idade']}")


print("\nPessoas Menores de Idade:")
for pessoa in menores_de_idade:
   print(f"Nome: {pessoa['nome']}, CPF: {pessoa['cpf']}, Idade: {pessoa['idade']}")
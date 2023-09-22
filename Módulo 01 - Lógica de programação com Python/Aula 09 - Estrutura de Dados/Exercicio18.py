"""18. Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um
ou mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes funções:
Adicionar contato: acrescenta um novo nome na agenda com um ou mais telefones.
Adicionar telefone: acrescenta um novo telefone em um nome já existente na agenda. Caso o nome não exista na agenda,
você deve perguntar se a pessoa deseja incluí-lo.
Excluir telefone: remove o telefone de uma pessoa que já está cadastrada na agenda.
Excluir contato: remove o nome de uma pessoa da agenda.
Consultar contato: obtém as informações de contato de uma pessoa pelo nome.
Listar contatos: listar todos os contatos (nome e telefones) presentes na agenda."""

agenda_telefonica = {}


while True:
   print("Bem-vindo à sua lista telefonica. Digite a opção desejada: \n")
   print("Opção 1: Adicionar contato. \n"
         "Opção 2: Adicionar telefone. \n"
         "Opção 3: Excluir telefone. \n"
         "Opção 4: Excluir contato. \n"
         "Opção 5: Consultar contato. \n"
         "Opção 6: Listar contato. \n"
         "Opção 7: Sair.\n")


   opcao = input("Digite o número da opção desejada: ")


   if opcao == "1":
       nome = input("Digite o nome do contato a ser adicionado: ")
       agenda_telefonica[nome] = []
       telefone = input(f"Digite o telefone de {nome}: ").split(" , ")
       agenda_telefonica[nome].append(telefone)
       print(f"{nome} foi adicionado à agenda com o telefone: {telefone}")


   elif opcao == "2":
       nome = input("Digite o nome do contato a receber o novo telefone: ")
       if nome in agenda_telefonica:
           novo_telefone = input(f"Digite o novo telefone de {nome}: ")
           agenda_telefonica[nome].append(novo_telefone)
           print(f"Novo telefone adicionado para {nome}: {novo_telefone}")
       else:
           print(f"{nome} não está na agenda.")


   elif opcao == "3":
       nome = input("Digite o nome do contato do qual deseja excluir um telefone: ")
       if nome in agenda_telefonica[nome]:
           print(f"Telefones de {nome}: {', '.join(agenda_telefonica[nome])}")
           telefone = input(f"Digite o telefone a ser removido de {nome}: ")
           if telefone in agenda_telefonica[nome]:
               agenda_telefonica[nome].remove(telefone)
               print(f"Telefone {telefone} removido.")
           else:
               print(f"{nome} não está na agenda.")
       else:
           print(f"{nome} não está na agenda.")


   elif opcao == "4":
       nome = input("Digite o nome do contato a ser excluído da agenda: ")
       if nome in agenda_telefonica:
           del agenda_telefonica[nome]
           print(f"{nome} foi removido da agenda.")
       else:
           print(f"{nome} não está na agenda.")


   elif opcao == "5":
       nome = input("Digite o nome do contato a ser consultado: ")
       if nome in agenda_telefonica:
           print(f"Nome: {nome} \n"
                 f"Telefones: {', '.join(agenda_telefonica[nome])}")
       else:
           print(f"{nome} não está na agenda.")


   elif opcao == "6":
       if len(agenda_telefonica) == 0:
           print("A agenda está vazia.")
       else:
           for nome, telefones in agenda_telefonica.items():
               print(f"Nome: {nome}")
               print(f"Telefones: {', '.join(agenda_telefonica[nome])}")
               print()


   elif opcao == "7":
       print("Saindo do programa.")
       break
   else:
       print("Opção inválida. Tente novamente.")
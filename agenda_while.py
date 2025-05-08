agenda = {}
contador = 1
while True:
    nome = input("digite o nome: ")
    telefone = input("digite o telefone: ")
    email = input("digite o email: ")

    chave = f"contato{contador}"
    agenda[chave] = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contador += 1

    continuar = input("deseja adicionar outro contato? (s/n): ")
    if continuar.lower() != 'n':
        break

    print("\nAgenda completa: ")
    for chave, dados in agenda.items():
        print(f"{chave}")
        print(f"nome={dados["nome"]}")
        print(f"telefone={dados["telefone"]}")
        print(f"email={dados["email"]}")
        print("-" * 20)

    with open("agenda.txt", "w") as arquivo:
        for chave, dados in agenda.items():
            arquivo.write(f"{chave}\n")
            arquivo.write(f" nome = {dados["nome"]}\n")
            arquivo.write(f" telefone = {dados["telefone"]}\n")
            arquivo.write(f" email = {dados["email"]}\n")
            arquivo.write("-" * 20 + "\n")

    print("agenda salva")
            
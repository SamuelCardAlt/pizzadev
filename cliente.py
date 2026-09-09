clientes = []

print("----- Cadastro Cliente -----")
nome=input("Digite seu nome: ").strip()
if nome == "":
    print("Erro! o nome não pode ser vazio")
else:
    telefone=input("Digite seu telefone: ").strip()
    if not telefone.isdigit():
        print("Erro! o telefone deve conter somente numeros! ")
    else:
        clientes=[nome,telefone]
        clientes.append(clientes)
        print("Cliente cadastrado com sucesso! ")

        print("----- Dados do cliente -----")
        print("-"*40)
        print(f"Nome: {nome}")
        print(f"Telefone: {telefone}")
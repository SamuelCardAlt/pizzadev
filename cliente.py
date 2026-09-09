clientes = []

print("-----Cadastro Cliente-----")
nome=input("Digite seu nome: ").strip()
if nome == "":
    print("Erro! o nome não pode ser vazio")
else:
    telefone=input("Digite seu telefone: ").strip()
    if not telefone.isdigit():
        print("Erro! o telefone deve conter somente numeros! ")
    else:

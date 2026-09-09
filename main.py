pizzas = ["calabresa","carne de sol","Frango com catupiry","Frango"]
precos= [30.00,40.00,30.00,29.90]
print("---- Menu ----")
print("---- Cardapio ----")

for indice in range(len(pizzas)):
    print(f"{indice +1} - {pizzas[indice]}: R${precos[indice]}")
escolha= input("digite sua escolha: ")
if escolha.isdigit():
    escolha=int(escolha)
    if 1 <= escolha <= len(pizzas):
        indice = escolha - 1
        print(f"você escolheu: {pizzas[indice]}")
        print(f"Preço: R$ {precos[indice]:.2f}")
    else:
        print("Opção inválida! Escolha um número do cardápio.")
else:
    print("Digite apenas o número da pizza.")

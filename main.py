pizzas = ["calabresa","carne de sol","Frango com catupiry"]
precos= [30.00,40.00,30.00]
print("---- Menu ----")
print("---- Cardapio ----")

for indice in range(len(pizzas)):
    print(f"{indice +1} - {pizzas[indice]}: R${precos[indice]}")
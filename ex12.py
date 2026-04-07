#Exercício 12 - Menu de opções com o uso de "Match Case"

print(f"{'MENU':^30}")
print("1 - Ver saldo disponível")
print("2 - Depositar um valor")
print("3 - Sair")

escolha = int(input("Qual a sua escolha?  "))

match escolha:
    case 1:
        print(f"O seu saldo disponível é de R$ XX")
    case 2:
        valor_de_deposito = float(input("Qual o valor do deposito? R$ "))
        print(f"Valor depositado! Saldo atualizado!")
    case 3:
        print("Volte sempre!")
    case _:
        print("Número inválido!")
#Exercício 5 - Perguntar o saldo bancário, perguntar o valor de saque, se tiver saldo = saque aprovado, senão, reprovado

saldo = float(input("Digite o seu saldo no banco: R$"))
valor_de_saque = float(input("Digite o valor para saque: R$"))

saldo_final = saldo - valor_de_saque
if valor_de_saque < saldo:
    print("Saque realizado!")
    print(f"O seu saldo agora é de: R${saldo_final}")
else:
    print("Saque reprovado!")
    print(f"O seu saldo continua sendo R$ {saldo}")
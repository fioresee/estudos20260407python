#Exercício 6 - Sistema de depósito perguntando o quanto que se deseja depositar e mostrar o saldo atualizado

saldo = 0
valor_de_deposito = float(input("Digite o valor do deposito: R$"))

saldo_final = saldo + valor_de_deposito
print(f"O seu saldo foi atualizado: De R${saldo} para R${saldo_final}")
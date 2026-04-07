#Exercício 8 - Pedir um valor vendido: Se vender mais de 1000 = comissão de 10%. senão, 5%

valor_vendido = float(input("Qual foi o valor que foi vendido? R$ "))
if valor_vendido > 1000:
    comissao = 0.1 * valor_vendido
else:
    comissao = 0.05 * valor_vendido

faturamento_total = valor_vendido + comissao
print(f"Valor vendido: R${valor_vendido:.2f}")
print(f"Comissão: R${comissao:.2f}")
print(f"O seu salário final tem o valor de: {faturamento_total:.2f}")
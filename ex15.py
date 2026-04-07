#Exercício 15 - Conversão Real para Dólar

valor_em_reais = float(input("Digite um valor em reais (R$): "))

valor_em_dolar = valor_em_reais / 5.15  #Consulta realizada em 07/04/2026 às 19:26

print(f"O valor digitado corresponde a U${valor_em_dolar:.2f}")

#Conversão Dólar para Real

valor_em_dolar2 = float(input("Digite um valor em dólares (U$): "))

valor_em_reais2 = valor_em_dolar2 * 5.15  #Consulta realizada em 07/04/2026 às 19:26

print(f"O valor digitado corresponde a R${valor_em_reais2:.2f}")

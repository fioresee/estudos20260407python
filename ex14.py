#Exercício 14 - Conversão de Tempo

valor_em_segundos = int(input("Digite um valor em segundos: "))

valor_em_minutos = valor_em_segundos / 60
valor_em_horas = valor_em_segundos / 3600
valor_em_dias = valor_em_segundos / 86400

print(f"O valor digitado corresponde a {valor_em_minutos:.3f} minutos!")
print(f"O valor digitado corresponde a {valor_em_horas:.3f} horas!")
print(f"O valor digitado corresponde a {valor_em_dias:.3f} dias!")
#Exercício 4 - Pedir um número e classificar ele em positivo, negativo ou zero

numero = int(input("Digite um número inteiro: "))

if numero == 0:
    print("O número é zero!")
elif numero < 0:
    print("O número é menor que zero. Portanto, negativo!")
else:
    print("O número é maior que zero. Portanto, positivo!")
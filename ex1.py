#Exercício 1 - Pedir um número e dizer se é par ou ímpar

#Utilizando Match Case

numero = int(input("Digite um número: "))

match numero % 2:
        case 0:
            print(f"O número {numero} é par!")
        case 1:
            print(f"O número {numero} é ímpar!")

#Utilizando If / Else

num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f"O número {num} é par!")
else:
    print(f"O número {numero} é ímpar!")
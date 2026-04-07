#Exercício 13 - Calculadora com "Match Case"

numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))

print(f"Os números escolhidos foram: {numero1, numero2}.\n")

print(f"{'MENU DE OPERAÇÕES':^30}")
print("[ 1 ] Somar")
print("[ 2 ] Subtrair")
print("[ 3 ] Multiplicar")
print("[ 4 ] Dividir")
escolha = int(input("Escolha uma das operações acima: "))

match escolha:
    case 1:
        print("Você escolheu a SOMA!")
        soma = numero1 + numero2
        print(f"A soma dos números escolhidos ({numero1} e {numero2}) equivale a {soma}!")
    case 2:
        print("Você escolheu a SUBTRAÇÃO!")
        sub = numero1 - numero2
        print(f"A subtração dos números escolhidos ({numero1} e {numero2}) equivale a {sub}!")
    case 3:
        print("Você escolheu a MULTIPLICAÇÃO!")
        mult = numero1 * numero2
        print(f"A multiplicação dos números escolhidos ({numero1} e {numero2}) equivale a {mult}!")
    case 4:
        if numero2 == 0:
            print("Erro: Não é possível dividir por zero.")
        else:
            print("Você escolheu a DIVISÃO!")
            div = numero1 / numero2
            print(f"A divisão dos números escolhidos ({numero1} e {numero2}) equivale a {div:.1f}!")
    case _:
        print("Valor inválido!")
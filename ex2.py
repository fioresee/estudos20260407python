#Exercício 2 - Pedir a idade do usuário e dizer se a pessoa é maior de idade ou não

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"Você tem {idade} anos. Portanto, você é maior de idade!")
elif idade < 18 and idade >= 2:
    print(f"Você tem {idade} anos. Portanto, você é menor de idade!")
elif idade == 1:
    print(f"Você tem {idade} ano. Portanto, você é menor de idade!")
elif idade < 0:
    print(f"Idade inválida! ({idade})")
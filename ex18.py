#Exercício 18 - Acesso ao sistema: Idade >= 18 E tem autorização

idade = int(input("Digite sua idade: "))
autorizacao = input("Você possui autorização? (S/N): ")

if idade >= 18 and autorizacao.lower() == "s":
    print("Acesso liberado!")
else:
    print("Acesso negado!")
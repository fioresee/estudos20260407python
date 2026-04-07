#Exercício 9 - Sistema de login com usuário e senha pré-definidos

tentativas = 0

print(f"{'BANCO':^30}")

while True:
    nome_de_usuario = input("Nome de usuário: ")
    senha = input("Senha: ")

    if nome_de_usuario.lower() != "admin" or senha != "1234":
        tentativas += 1
        print("Usuário ou senha incorretos!")

    else:
        print("Login realizado com sucesso!")
        break
    if tentativas == 3:
        print("Tentativas esgotadas! Tente novamente mais tarde.")
        break
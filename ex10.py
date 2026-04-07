#Exercício 10 - Verificação de senha = menor que 6 dígitos é inválida


nome_de_usuario = input("Nome de usuário: ")
senha = input("Senha: ")

if len(senha) < 6:          # "len(senha)" conta quantos caracteres a senha possui
    print("Senha inválida!")
else:
    print("Senha válida!")


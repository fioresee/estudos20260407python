#Exercício 19 - Sistema básico de uma loja

tentativas = 0

print(f"{'LOJA':^30}")

while True:

    nome_de_usuario = input("Digite seu nome de usuário: ")
    senha = int(input("Digite sua senha: "))

    if nome_de_usuario != "admin" or senha != 1234:
        tentativas += 1
        print("Usuário ou senha incorretos!")

    else:
        print("Login realizado com sucesso!")
        print("Escolha seu produto: ")
        print("1 - Maçã (R$ 3.00)")
        print("2 - Banana (R$ 2.50)")
        print("3 - Laranja (R$ 4.00)")

        escolha_fruta = int(input("Digite sua escolha: "))
        quantidade = int(input("Digite a quantidade que deseja adquirir: "))

        preco_maca = 3.0
        preco_banana = 2.5
        preco_laranja = 4.0

        if escolha_fruta == 1:
            valor_final = preco_maca * quantidade

        elif escolha_fruta == 2:
            valor_final = preco_banana * quantidade

        elif escolha_fruta == 3:
            valor_final = preco_laranja * quantidade

        else:
            print("Opção inválida!")
            break

        print(f"Resumo da compra: Quantidade: {quantidade}. Valor: R$ {valor_final:.2f}")

        cadastro = input("Possui cadastro na loja? (S/N) ")

        if cadastro.lower() == "s":
            print("Você possui um desconto de 5%!")
            valor_final = valor_final * 0.95  # ✅ agora ATUALIZA o valor
            print(f"Valor com desconto: R$ {valor_final:.2f}")
        else:
            print(f"Valor final: R$ {valor_final:.2f}")

        saldo_conta = float(input("Informe o seu saldo: R$ "))

        if saldo_conta < valor_final:
            print("Você não possui saldo suficiente para comprar!")
        else:
            saldo_conta_final = saldo_conta - valor_final
            print(f"Compra realizada com sucesso!")
            print(f"Saldo atual: R$ {saldo_conta_final:.2f}")

        break

    if tentativas == 3:
        print("Tentativas esgotadas!")
        break
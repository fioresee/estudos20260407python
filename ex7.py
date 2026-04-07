#Exercício 7 - Loja com desconto Produto custa R$100. Pagamento à vista = 10% de desconto, senão preço normal

preco = 100
forma_de_pagamento = input("A forma de pagamento será à vista? ").lower()
if forma_de_pagamento == "sim" or forma_de_pagamento == "s":
    preco_com_desconto = preco * 0.9
    print(f"O preço final será de R${preco_com_desconto:.2f}")
else:
    print(f"O preço final permanece em R$100")
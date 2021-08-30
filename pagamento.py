print('{:=^40}'.format('RF LOJAS')) # '{:=^40'} centraliza o texto em 40 espaços e com o sinal de '='
                                    # entre os espaços.


def pagamento():

    # VALOR DO PRODUTO:
    preco = float(input("Digite o valor do produto: "))
    print("O valor original do produto é R$ {}.".format(preco))

    # FORMA DE PAGAMENTO:
    print('''Forma de pagamento:
          [1] À vista dinheiro/débito (10% de desconto)
          [2] À vista no cartão de crédito (5% de desconto)
          [3] Em 2x sem juros (preço normal)
          [4] 3x ou mais no cartão (20% de juros)''')
    opcao = int(input("Digite a forma de pagamento: "))

    # CÁLCULO DO DESCONTO OU JUROS:
    while opcao > 4 or opcao < 1:
        print("Opção inválida, digite novamente:")
        print('''Forma de pagamento:
                  [1] À vista dinheiro/débito (10% de desconto)
                  [2] À vista no cartão de crédito (5% de desconto)
                  [3] Em 2x sem juros (preço normal)
                  [4] 3x ou mais no cartão (20% de juros)''')
        opcao = int(input("Digite a forma de pagamento: "))
    if opcao == 1:
        preco = preco - (preco * 0.1)
        print("Para a opção à vista, o novo valor do produto será de R$ {:.2f}.".format(preco))
    elif opcao == 2:
        preco = preco - (preco * 5/100)
        print("Para a opção à vista no cartão de crédito, o novo valor do produto será de R$ {:.2f}.".format(preco))
    elif opcao == 3:
        print("Para o pagamento em 2x no cartão de crédito, o produto ficará com o valor original.")
    elif opcao == 4:
        vezes = int(input("Quantas vezes será o parcelamento? "))
        preco = preco + (preco * 20/100)
        parcela = preco / vezes
        print("Para o parcelamento em {} vezes, o valor do produto será de R$ {:.2f}.".format(vezes, preco))
        print("O valor mensal da parcela será de R$ {:.2f}.".format(parcela))


pagamento()

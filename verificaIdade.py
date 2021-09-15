# verifica em um grupo de pessoas quantas atingiram a maior idade (<20 anos) e quantas não atingiram

from datetime import date


def idade():
    anoAtual = date.today().year
    maior = 0
    menor = 0
    for c in range(1, 8):
        nasc = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(c)))
        idade = anoAtual - nasc
        if idade >= 21:
            maior += 1
        else:
            menor += 1
    print("{} pessoas já atingiram a maioridade.\n{} pessoas ainda não atingiram a maioridade.".format(maior, menor))


idade()

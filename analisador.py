# Criação de um programa para analisar características de determinado grupo de pessoas definido pelo usuário
# O programa deve mostrar o homem mais velho do grupo, a quantidade de mulheres com menos de 20 anos
# e a média de idade do grupo.


def analisador():
    # Inicializando a variável do homem mais velho do grupo:
    homemvelho = ''
    # Inicializando a variável da pessoa de maior idade:
    maioridade = 0
    # Inicializando a variável da soma das idades:
    soma = 0
    # Inicializando a variável do contador:
    c = 0
    for p in range(1, 7):
        print('DADOS DA {}ª PESSOA'.format(p))
        nome = str(input("Nome: ")).strip()
        idade = int(input("Idade: "))
        sexo = str(input("Sexo [M/F]: ")).strip().upper()
        soma += idade
        # Identificando o homem mais velho do grupo:
        if p == 1 and sexo == 'M':
            homemvelho = nome
            maioridade = idade
        if idade > maioridade and sexo == 'M':
            maioridade = idade
            homemvelho = nome
        # Identificando a quantidade de mulheres com menos de 20 anos:
        if idade < 20 and sexo == 'F':
            c += 1
    # Média de idade do grupo
    media = soma / 7

    print("O homem mais velho é {} e tem {} anos.".format(homemvelho, maioridade))
    print("Neste grupo existem {} mulheres com menos de 20 anos.".format(c))
    print("A média de idade do grupo é de {:.1f} anos".format(media))


analisador()

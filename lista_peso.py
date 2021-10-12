# PROGRAMA QUE ANALISA DADOS DE PESO INCLUÍDOS

pessoas = []
dados = []


# PRIMEIRA MANEIRA (VERIFICANDO PESSOAS COM MAIS DE 80 KG E MENOS DE 80 KG:
def peso():
    maiorPeso = []
    maisLeve = []
    contmp = contml = 0
    while True:
        dados.append(str(input("Digite o nome: ")).strip())
        dados.append(float(input("Digite o peso: ")))
        pessoas.append(dados[:])
        escolha = str(input("Deseja continuar (S/N)? ")).strip().upper()[0]
        dados.clear()
        while 'N' not in escolha and 'S' not in escolha:
            escolha = str(input("Escolha inválida. Digite S para continuar ou N para encerrar: ")).strip().upper()[0]
        if escolha == 'N':
            break
    print(f'Foram cadastradas {len(pessoas)} pessoas.')

    for mp in pessoas:
        if mp[1] > 80:  # Verifica na lista quais pessoas tem mais de 80 quilos
            maiorPeso.append(mp[0])
            contmp += 1
        else:
            maisLeve.append(mp[0])
            contml += 1
    print(f'{contmp} pessoas tem mais de 80Kg. São: {maiorPeso}.')
    print(f'{contml} pessoas tem menos de 80Kg. São: {maisLeve}.')


# SEGUNDA MANEIRA (COMO SABER O MENOR E MAIOR PESO):
def peso2():
    maior = menor = 0
    while True:
        dados.append(str(input("Digite o nome: ")).strip())
        dados.append(float(input("Digite o peso: ")))
        if len(pessoas) == 0:  # Define o maior e menor peso iniciais quando a lista "pessoas" não tiver sido alimentada
            maior = menor = dados[1]  # Define que o maior e menor peso serão igual ao primeiro
            # valor da posição 1 de "dados"
        else:
            if dados[1] > maior:  # Define o maior peso caso este seja maior que o dado inicial
                maior = dados[1]
            if dados[1] < menor:
                menor = dados[1]  # Define p menor peso, caso este seja menor que o dado inicial
        pessoas.append(dados[:])
        escolha = str(input("Deseja continuar (S/N)? ")).strip().upper()[0]
        dados.clear()
        while 'N' not in escolha and 'S' not in escolha:
            escolha = str(input("Escolha inválida. Digite S para continuar ou N para encerrar: ")).strip().upper()[0]
        if escolha == 'N':
            break
    print(f'Foram cadastradas {len(pessoas)} pessoas.')
    print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
    for mp in pessoas:  # Verifica qual a pessoa da lista que possui maior peso
        if mp[1] == maior:
            print(f'{[mp[0]]} ', end='')
    print()
    print(f'O menor peso foi de {menor} Kg. Peso de ', end='')
    for ml in pessoas:  # Verifica qual a pessoa da lista que possui menor peso
        if ml[1] == menor:
            print(f'{[ml[0]]} ', end='')


peso()
peso2()

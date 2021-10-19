# CADASTRO E ESTATÍSTICAS DE JOGADORES

estatisticas = []  # Lista para armazenar as estatísticas que o programa vai ler
# CADASTRANDO JOGADORES...
while True:
    gols = []  # Lista que armazena os gols feitos por partida de cada jogador
    nome = str(input("Nome do jogador: "))
    jogos = int(input("Número de partidas jogadas: "))
    print('-' * 30)
    jogador = {'Nome': nome, 'Jogos': jogos}  # Dicionário que armazena as estatísticas de cada jogador
    totalgols = 0
    for g in range(jogos):  # Lê a quantidade de gols feitos em cada partida que o jogador cadastrado jogou
        gols.append(int(input(f'Nº de gols marcados por {jogador["Nome"]} na partida {g + 1}: ')))
    print('-' * 30)
    jogador['Gols'] = gols  # Adiciona os gols feitos por partida dentro do dicionário "Jogador"
    totalgols = sum(gols)  # Soma do total de gols
    jogador['Total de gols'] = totalgols  # Adiciona a estatística de total de gols dentro do dicionário "Jogador"
    estatisticas.append(jogador.copy())  # Insere o dicionário dentro de uma lista
# VERIFICANDO SE O USUÁRIO DESEJA CADASTRAR MAIS JOGADORES...
    escolha = str(input("Digite S para cadastrar mais jogadores ou N para parar: ")).strip().upper()[0]
    while 'N' not in escolha[0] and 'S' not in escolha[0]:
        escolha = str(input("Digite uma opção válida. S para continuar ou N para parar: ")).strip().upper()[0]
    if escolha[0] == 'N':
        break
# ESCREVENDO AS ESTATÍSTICAS DOS JOGADORES CADASTRADOS...
print('=' * 20, 'ESTATÍSTICAS', '=' * 20)
print(f'{"ID":<4}{"NOME":^8}{"JOGOS":^10}{"GOLS":^10}{"TOTAL DE GOLS":>10}')
# Acessando a lista de dicionários para escrever as estatísticas de todos os jogadores
for i, j in enumerate(estatisticas):
    print(f'{i + 1:<4}', end='')
    for d in j.values():
        print(f'{str(j["Nome"]):^8}{str(j["Jogos"]):^10}{str(j["Gols"]):^10}'
              f'{str(j["Total de gols"]):>10}')
        break
# VISUALIZAÇÃO DA ESTATÍSTICA INDIVIDUAL DE CADA JOGADOR
while True:
    print('=' * 40)
    ID = int(input("Digite o ID do jogador para visualizar os dados individualmente. "
                   "(Digite 0 para encerrar o programa): "))
    # ID = CÓDIGO DO JOGADOR QUE É MOSTRADO EM "ESCREVENDO AS ESTATÍSTICAS DOS JOGADORES CADASTRADOS"
    while ID > len(estatisticas):
        ID = int(input("Opção inválida!. Escolha uma opção válida, ou 0 para encerrar o programa: "))
    if ID == 0:
        print('=' * 25, 'PROGRAMA ENCERRADO', '=' * 25)
        break
    # Acessando a lista de dicionários
    for i, a in enumerate(estatisticas):
        if ID == i + 1:
            print(f'-- ESTATÍSTICAS DO JOGADOR {a["Nome"]}:')
            # Acessando a lista "Gols", dentro do dicionário Estatísticas
            for p, m in enumerate(a["Gols"]):
                print(f'--> Na {p + 1}ª partida, fez {m} gols.')

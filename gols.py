gols = []
nome = str(input("Nome do jogador: "))
jogos = int(input("Número de partidas jogadas: "))
jogador = {'Nome': nome, 'Jogos': jogos}
totalgols = 0
for g in range(jogos):
    gols.append(int(input(f'Nº de gols marcados por {jogador["Nome"]} na partida {g + 1}: ')))
totalgols = sum(gols)
jogador['Total de gols'] = totalgols
print('=' * 30)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Jogos"]} partidas.')
for p, g in enumerate(gols):
    print(f'{"=>":>5} Na {p + 1}ª partida, fez {g} gols.')
print(f'Foi um total de {jogador["Total de gols"]} gols.')

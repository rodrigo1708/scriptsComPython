# JOGO DE DADOS - 4 jogadores jogam um dado e, no final, será mostrada a classificação dos jogadores

from operator import itemgetter
from random import randint
from time import sleep

jogo = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6)}  # Cria os 4 jogadores com o sorteio de cada numero do
                                                                    # dado para cada jogador
ranking = {}
print('='*15, 'VALORES SORTEADOS', '='*15)
for k, v in jogo.items():
    print(f'{k} tirou o valor {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # Coloca o ranking dos jogadores de acordo com
                                                                # a pontuação. Maior pontuação >> menor pontuação
print('='*15, 'RANKING', '='*15)
sleep(1)
for k, v in enumerate(ranking):
    print(f'{k + 1}º colocado: {v[0]} ==> {v[1]} pontos.')
    sleep(1)
print('='*40)
print('<< PROGRAMA FINALIZADO >>')

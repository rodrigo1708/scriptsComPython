from random import randint

print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("Escolha sua opção: "))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print("Computador jogou {}.".format(itens[pc]))
print("Jogador jogou {}.".format(itens[jogador]))
if pc == 0: #pc jogou pedra
    if jogador == 0:
        print("EMPATE.")
    elif jogador == 1:
        print("JOGADOR GANHA.")
    elif jogador == 2:
        print("COMPUTADOR GANHA.")
    else:
        print("Jogada inválida")
elif pc == 1: #Pc jogou papel
    if jogador == 0:
        print("COMPUTADOR GANHA.")
    elif jogador == 1:
        print("EMPATE.")
    elif jogador == 2:
        print("JOGADOR GANHA.")
    else:
        print("Jogada inválida")
elif pc == 2: #pc jogou tesoura
    if jogador == 0:
        print("JOGADOR GANHA.")
    elif jogador == 1:
        print("COMPUTADOR GANHA.")
    elif jogador == 2:
        print("EMPATE.")
    else:
        print("Jogada inválida")
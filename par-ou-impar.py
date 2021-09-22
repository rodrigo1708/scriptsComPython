# CRIAÇÃO DO PROGRAMA PAR OU ÍMPAR

from random import randint
from time import sleep
vitoria = 0
print("="*30)
print("VAMOS JOGAR PAR OU ÍMPAR!")
print("="*30)
sleep(1)
while True: # loop infinito caso o jogador vença o computador
    # O jogador escolhe "par" ou "ímpar". Se digitar uma palavra, o código armazenará apenas a primeira letra, colocará em maiúscula e retira todos os espaços.
    escolha = str(input("Digite 'p' se quiser par ou 'i' se quiser ímpar: ")).strip().upper()[0]
    # Caso a variável escolha seja preenchida errada, é criado o loop infinito até que o jogador digite uma entrada válida
    while escolha != 'P' and escolha != 'I':
        escolha = str(input("Digite uma opção válida! (P para PAR ou I para ÍMPAR): ")).strip().upper()[0]
    jogador = int(input("Qual número você quer jogar? "))
    # O computador joga um número aleatório no intervalo de 0 a 10.
    pc = randint(0, 10)
    soma = jogador + pc
    # Código para verificar se a soma dos valores jogados pelo jogador e pelo pc é par ou ímpar.
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print("-"*50)
    print(f'Você jogou {jogador} e o computador jogou {pc}. A soma deu {soma}. {resultado}!')
    print("-"*50)
    sleep(2)
    # Se o resultado for igual à escolha do jogador (par ou ímpar), o jogador vence a primeira partida e o loop começa de novo.
    if resultado[0] == escolha:
        sleep(1)
        print("\o/"*5)
        print("Você venceu!!\nVamos jogar novamente...")
        print("=-="*15)
        sleep(2)
        vitoria += 1
    # Caso o resultado seja diferente da escolha do jogador, o pc vence e o loop se encerra.
    else:
        break
print("-_-"*15)
# Em caso de vitória do pc, o programa conta quantaas vitórias o jogador teve até perder para o pc.
if vitoria >= 5:
    print(f"GAME OVER!\nPARABÉNS você venceu {vitoria} vezes!!")
else:
    print(f"GAME OVER! Você venceu {vitoria} vezes.")

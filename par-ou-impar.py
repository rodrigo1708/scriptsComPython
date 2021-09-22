from random import randint
from time import sleep
vitoria = 0
print("="*30)
print("VAMOS JOGAR PAR OU ÍMPAR!")
print("="*30)
sleep(1)
while True:
    escolha = str(input("Digite 'p' se quiser par ou 'i' se quiser ímpar: ")).strip().upper()[0]
    while escolha != 'P' and escolha != 'I':
        escolha = str(input("Digite uma opção válida! (P para PAR ou I para ÍMPAR): ")).strip().upper()[0]
    jogador = int(input("Qual número você quer jogar? "))
    pc = randint(0, 10)
    soma = jogador + pc
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print("-"*50)
    print(f'Você jogou {jogador} e o computador jogou {pc}. A soma deu {soma}. {resultado}!')
    print("-"*50)
    sleep(2)
    if resultado[0] == escolha:
        sleep(1)
        print("\o/"*5)
        print("Você venceu!!\nVamos jogar novamente...")
        print("=-="*15)
        sleep(2)
        vitoria += 1
    else:
        break
print("-_-"*15)
if vitoria >= 5:
    print(f"GAME OVER!\nPARABÉNS você venceu{vitoria} vezes!!")
else:
    print(f"GAME OVER! Você venceu {vitoria} vezes.")

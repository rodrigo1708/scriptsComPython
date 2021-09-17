from random import randint
from time import sleep
print('-=-'*5, 'Jogo da Adivinhação', '-=-'*5)
print('Pensando em um número de 0 a 10...')
sleep(2)
escolha = randint(0, 10)
n = int(input("Em qual número pensei? "))
contador = 1
while n != escolha:
    if n < escolha:
        print("Tá frio, aumente o palpite.")
    else:
        print("Tá quente, diminua o palpite.")
    continua = str(input("Quer tentar novamente [S/N]? ")).strip().upper()[0]
    if continua == 'S':
        n = int(input("Tente adivinhar o número que pensei: "))
        contador += 1
    else:
        print("Ganhei! Eu pensei no número {}.".format(escolha))
        break
if n == escolha:
    print("Parabéns!! Você adivinhou o número que pensei após {} tentativa(s)!!".format(contador))

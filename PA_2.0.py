# GERADOR DE PROGRESSÃO ARITMÉTICA
from time import sleep

a1 = 0
an = 0
enesimo = 0
razao = 0
escolha = 0
while escolha != 4:
    print("="*15, "Gerador de Progressão Artimética", "="*15)
    print('''Escolha o que você quer fazer: 
            [ 1 ] - Descobrir o primeiro termo da progressão;
            [ 2 ] - Descobrir a razão da progressão;
            [ 3 ] - Descobrir o valor do enésimo termo da progressão;
            [ 4 ] - Sair do programa.''')
    escolha = int(input("Escolha sua opção: "))
    while escolha > 4 or escolha == 0:
        escolha = int(input("Digite uma opção válida: "))
    if escolha == 1:
        enesimo = int(input("Qual o último termo da progressão? "))
        an = int(input("Qual o valor do último termo? "))
        razao = int(input("Digite a razão da progressão? "))
        a1 = an - razao * (enesimo - 1)
        print("O primeiro termo da P.A. é {}.".format(a1))
        sleep(3)
    elif escolha == 2:
        a1 = int(input("Qual o valor do primeiro termo? "))
        an = int(input("Qual o valor do último termo? "))
        enesimo = int(input("Qual o último termo da progressão? "))
        razao = (an - a1) / (enesimo - 1)
        print("A razão da P.A. é {}.".format(razao))
        sleep(3)
    elif escolha == 3:
        enesimo = int(input("Digite o termo que você quer descobrir o valor: "))
        razao = int(input("Digite a razão da P.A.: "))
        a1 = int(input("Digite o valor do primeiro termo da P.A.: "))
        an = a1 + (enesimo - 1) * razao
        for n in range(1, enesimo + 1):
            c = a1 + (n - 1) * razao
            print("A{} = {}".format(n, c), end=' -> ')
        print("Fim", end='',)
        print("\nO termo a{} tem valor {}".format(enesimo, c))
        sleep(3)
print("Você escolheu finalizar o programa...")
sleep(2)
print("Programa finalizado!")

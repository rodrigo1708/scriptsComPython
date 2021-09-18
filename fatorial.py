from time import sleep
from math import factorial


# CALCULANDO O FATORIAL COM WHILE
def fatwhile():
    n = int(input("Digite um número para calcular o seu fatorial: "))
    print("Calculando...")
    sleep(2)
    print("O fatorial de {} é:\n{}! = ".format(n, n), end='')
    fatorial = 1  # Declarando a variável que multiplicará os termos
    while n > 0:
        sleep(1)
        print("{}".format(n), end='')
        if n > 1:
            print(' x ', end='')
        else:
            print(' = ', end='')
        fatorial *= n
        n -= 1
    sleep(1)
    print(fatorial)


# CALCULANDO FATORIAL COM FOR:
def fatfor():
    n = int(input("Digite um número para o cálculo do fatorial: "))
    print("Calculando...")
    print("{}! = ".format(n), end='')
    sleep(2)
    for p in range(n, 0, -1):  # Customização da resposta do programa (Contagem regressiva para mostrar os termos)
        if p == 1:
            print("{} = ".format(p), end='')
        else:
            print("{} x ".format(p), end='')
        sleep(1)
    for f in range(1, n):  # Resolvendo o fatorial com FOR
        n *= f
    print(n)


# CALCULANDO FATORIAL COM A BIBLIOTECA FACTORIAL
def mathfat():
    n = int(input("Digite o número para calcular o fatorial: "))
    print("{}! = {}".format(n, factorial(n)))


fatfor()
fatwhile()
mathfat()

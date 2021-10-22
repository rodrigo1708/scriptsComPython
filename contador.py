from time import sleep


def linha():
    print('=' * 40)


def contador(i, f, c):
    while c == 0:
        c = int(input("Escolha um valor diferente de 0: "))
    if c < 0:
        c *= -1
    linha()
    print(f'Contagem de {i} até {f}, de {c} em {c}:')
    if i < f:
        p = i
        while p <= f:
            print(p, end=' ')
            sleep(0.5)
            p += c
    else:
        p = i
        while f <= p:
            print(p, end=' ')
            sleep(0.5)
            p -= c
    print('FIM!')


# PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input("Início: "))
fim = int(input("Fim: "))
cont = int(input("Contador: "))
contador(inicio, fim, cont)

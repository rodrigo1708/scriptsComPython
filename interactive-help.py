from time import sleep

c = ('\033[m',  # Posição 0 - Sem cor
     '\033[1;97;41m',  # Posição 1 - Cor de fundo vermelha
     '\033[1;97;42m',  # Posição 2 - Cor de fundo verde
     '\033[1;97;46m',  # Posição 3 - Cor de fundo azul
     '\033[7;40m'      # Posição 4 - Cor de fundo branca
     )  # Definição de uma tupla de cores para personalização do manual interativo


def escreva(msg, cor=0):  # Função que escreve alguma mensagem passada
    """
    --> Função para escrever uma mensagem na tela
    :param msg: Mensagem que será mostrada na tela
    :param cor: cor a ser definida de acordo com a variável global "c" definida incialmente
    """
    tam = len(msg) + 10
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


def python(bib):  # Função que escreve a bilbioteca ou função em python que for escolhida pelo usuário
    """
    --> Função que escreve o manual de alguma biblioteca ou função
    :param bib: Biblioteca ou função a ser inserida
    """
    escreva(f"Acessando o manual do comando '{bib}'", 3)
    sleep(2)
    print(c[4], end='')
    help(bib)
    print(c[0], end='')


while True:  # Programa principal que recebe as entradas do usuário
    escreva('Sistema de ajuda PyHELP', 2)  # Chamando a função escreva, que vai mostrar na tela a frase passada
    # (primeiro parâmetro), com a cor como segundo parâmetro
    man = str(input('Função ou biblioteca > '))
    python(man)  # Chamando a funçaõ que vai mostrar o manual escolhido pelo usuário
    sleep(1)
    escolha = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    while 'S' not in escolha[0] and 'N' not in escolha[0]:
        escolha = str(input('\033[0;31mOpção inválida! '
                            'Digite S para continuar ou N para encerrar o programa: \033[m')).strip().upper()[0]
    if escolha[0] == 'N':
        escreva('FIM DO PROGRAMA. ATÉ LOGO!', 1)
        sleep(1)
        break

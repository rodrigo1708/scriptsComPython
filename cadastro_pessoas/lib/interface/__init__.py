cadastro = []
c = ('\033[m',  # Posição 0 = sem cor
     '\033[0;33m',  # Posição 1 = Amarelo
     '\033[0;34m',  # Posição 2 = Azul
     '\033[0;31m',  # Posição 3 = Vermelho
     )


def linha(tam=42):
    return '-' * tam


def leiaint(msg):
    while True:
        n = str(input(msg)).strip()
        if n.replace('-', '').isnumeric():
            return int(n)
        else:
            print(f'{c[3]}Erro! Digite um número inteiro válido.{c[0]}')


def titulo(msg):
    print(linha(42))
    print(msg.center(42))
    print(linha(42))


def menu():
    opcoes = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema']
    titulo('MENU PRINCIPAL')
    for i, o in enumerate(opcoes):
        indice = i + 1
        print(f'{c[1]}{indice} - {c[0]}{c[2]}{o}{c[0]}')
    print(linha())
    opc = leiaint(f'{c[1]}Sua opção: {c[0]}')
    return opc



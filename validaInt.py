# VALIDANDO ENTRADA DE NÚMEROS INTEIROS


def leiaint(msg):
    """
    --> Função que faz a validação da entrada de dados do tipo inteiro (int)
    :param msg: Mensagem para entrada de dados do usuário
    :return: retorna o valor digitado, caso este tenha sido um número inteiro
    :print: Escreve uma mensagem de erro na tela, caso o valor digitado não seja do tipo inteiro
    """
    while True:
        n = str(input(msg)).strip()
        if n.replace('-', '').isnumeric():
            return int(n)
        else:
            print(f'\033[0;31mErro! Digite um número inteiro válido.\033[m')


# Programa principal
num = leiaint('Digite um número: ')
print(f'Você digitou o número {num}.')

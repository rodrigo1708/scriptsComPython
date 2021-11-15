# VALIDANDO ENTRADA DE NÚMEROS INTEIROS E DECIMAIS


def leiaint(inteiro):
    """
    --> Função que faz a validação da entrada de dados do tipo inteiro (int)
    :param inteiro: Mensagem para entrada de dados do usuário
    :return: retorna o valor digitado, caso este tenha sido um número inteiro
    :print: Escreve uma mensagem de erro na tela, caso o valor digitado não seja do tipo inteiro
    """
    while True:
        try:
            n = int(input(inteiro))
            return n
        except (TypeError, ValueError):
            print(f'\033[0;31mErro! Digite um número inteiro válido.\033[m')


def leiafloat(decimal):
    """
    --> Função que faz a validação da entrada de dados do tipo float
    :param decimal: Dados de entrada do usuário
    :return: Retorna o valor digitado pelo usuário, caso correto
    :print: Retorna mensagem de erro caso o dado de entrada não seja do tipo float
    """
    while True:
        try:
            f = float(input(decimal))
            return f
        except (TypeError, ValueError):
            print(f'\033[0;31mErro! Digite um número real válido!\033[m')


# Programa principal
num = leiaint('Digite um número inteiro: ')
real = leiafloat('Digite um número real: ')
print(f'Você digitou o número inteiro {num} e o número decimal {real}.')

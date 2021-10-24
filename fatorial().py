# CÁLCULO DE FATORIAL COM FUNÇÃO

def fatorial(num, esc):
    """
    --> Função de cálculo de fatorial de um número escolhido pelo usuário
    :param num: O número a ser calculado
    :param esc: O usuário escolhe se quer ou não visualizar o cálculo do fatorial
    :var f: Recebe o valor total do fatorial
    :var show: Define se o cálculo do fatorial será ou não mostrado na tela de resultado
    :print: Mostra os operadores matemáticos de acordo com o valor do número na regressão fatorial
    :return: Retorna o valor total do fatorial (f)
    """
    print('=' * 30)
    if esc == 'S':
        show = True
    else:
        show = False
    f = 1
    for n in range(num, 0, -1):
        f *= n
        if show:
            if n == 1:
                print(n, end=' = ')
            else:
                print(n, end=' x ')
    return f


# Programa principal
help(fatorial)
numero = int(input("Qual será o número fatorial? "))
escolha = str(input(f"Deseja visualizar a sequencia fatorial de {numero} (S/N)? ")).strip().upper()[0]
while 'S' not in escolha[0] and 'N' not in escolha[0]:
    escolha = str(input("Opção inválida! Escolha S para ver a sequência fatorial ou N para não ver: ")
                  ).strip().upper()[0]
print(fatorial(numero, escolha))

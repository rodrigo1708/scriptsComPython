#ESTRUTURA DE REPETIÇÃO FOR - VERIFICANDO NÚMEROS PRIMOS:

#VERIFICANDO QUAIS NÚMEROS SÃO PRIMOS EM UM RANGE DEFINIDO PELO USUÁRIO:
def range_primos():
    a = int(input("Digite um número: "))
    for x in range(a+1):
        div = 0
        for i in range(1, x+1):
            resto = x % i
            if resto == 0:
                div += 1
        if div == 2:
            print(x, "é número primo.")
        else:
            print(x, "não é número primo.")


#VERIFICANDO SE O NÚMERO DIGITADO PELO USUÁRIO É PRIMO:
def primo():
    n = int(input("Digite o número: "))
    c = 0

    for p in range(1, n + 1):
        resto = n % p
        if resto == 0:
            # Definindo a cor azul para quando o número digitado pelo usuário for divisível por P
            print('\033[34m',p, end=' ')
            c += 1
        else:
            # Definindo a cor vermelha para quando o número digitado pelo usuário NÃO for divisível por P
            print('\033[31m', p, end=' ')
    # Retirando o esquema de cor definido anteriormente
    print("\n\033[mO número {} tem divisão com resto zero {} vezes.".format(n, c))
    if c == 2:
        print("O número {} é primo.".format(n))
    else:
        print("O número {} não é primo.".format(n))


range_primos()
print("")
primo()

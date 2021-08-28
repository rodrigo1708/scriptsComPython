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
    a = int(input("Digite um número: "))
    div = 0
    for i in range(1, a+1):
        resto = a % i
        if resto == 0:
            div += 1
    if div == 2:
        print(a, "é número primo.")
    else:
        print(a, "não é número primo.")


range_primos()
print("")
primo()

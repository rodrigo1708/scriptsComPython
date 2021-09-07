def tabuada1():
    n = int(input("Digite qual a tabuada: "))
    mult = 0
    print("A tabuada de {} é: ".format(n))
    for c in range(1, 11):
        mult = n * c
        print("{} x {} = {}".format(n, c, mult))


# Código simplificado
def tabuada2():
    n = int(input("Digite o número da tabuada: "))
    for c in range(1, 11):
        print("{} x {} = {}".format(n, c, n*c))


tabuada1()
tabuada2()

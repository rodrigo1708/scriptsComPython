# PROGRAMA QUE LÊ 5 NÚMEROS E COLOCA EM ORDEM CRESCENTE.

numeros = []

for i in range(0, 5):
    n = int(input("Digite um número inteiro: "))
    if i == 0 or n > numeros[-1]:  # Insere o primeiro número na lista e/ou o último
        numeros.append(n)
    else:  # Percorrendo a variável "números" para verificar a posição que o número inserido será colocado.
        posicao = 0
        while posicao < len(numeros):
            if n <= numeros[posicao]:
                numeros.insert(posicao, n)
                break
            posicao += 1
print(numeros)

# PROGRAMA QUE LÊ 7 NUMEROS E ORDENA EM PAR E ÍMPAR

numeros = [[], []]

for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print(f'Foram digitados os números: ', end='')
for n in numeros:
    for m in n:
        print(m, end=' ')
print(f'\nSão pares: {sorted(numeros[0])}.\nSão ímpares: {sorted(numeros[1])}.')

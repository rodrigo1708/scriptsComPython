# PROGRAMA PARA ANALISAR NÚMEROS DIGITADOS EM UMA LISTA

numeros = []
cont = 0

while True:
    n = int(input("Digite um número inteiro: "))
    numeros.append(n)
    escolha = str(input("Deseja incluir mais números? (S/N) ")).upper().strip()[0]
    while 'S' not in escolha and 'N' not in escolha:
        escolha = str(input(
            "Digite uma opção válida (S para continuar ou N para encerrar o programa): ")
        ).upper().strip()[0]
    if escolha[0] == 'N':
        break
print('='*40)
print(f'Os números digitados foram: {numeros}')
print(f'Foram digitados {len(numeros)} numeros.')
print(f'Os valores digitados, em ordem crescente: {sorted(numeros)}.')
print(f'Os valores digitados em ordem decrescente: {sorted(numeros, reverse=True)}')
for c in numeros:
    if c == 5:
        cont += 1
if cont > 0:
    print(f'O número 5 faz parte da lista e foi digitado {cont} vezes.')
else:
    print(f'O número 5 não foi encontrado.')

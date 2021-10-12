# DIVIDINDO UMA LISTA EM LISTAs COM NÚMEROS PARES E NÚMEROS ÍMPARES

lista = []
listap = []
listai = []

while True:
    lista.append(int(input("Digite um número inteiro: ")))
    escolha = str(input("Deseja continuar? (S/N) ")).strip().upper()[0]
    while 'S' not in escolha and 'N' not in escolha:
        escolha = str(input("Digite uma opção válida! (S para continuar ou N para parar): ")).strip().upper()[0]
    if escolha[0] == 'N':
        break
print('='*40)
print(f'Os números digitados foram: {lista}.')
for p in lista:  # Verificando se o número da lista é par ou ímpar.
    if p % 2 == 0:
        listap.append(p)
    elif p % 2 != 0:
        listai.append(p)
print('='*40)
print(f'Os números pares digitados foram: {listap}.')
print(f'Os números ímpares digitados foram: {listai}.')

# CRIAÇÃO DE PROGRAMA QUE LÊ NÚMEROS DIGITADOS PELO USUÁRIO, ARMAZENA EM UMA LISTA E INFORMA O MAIOR E MENOR NÚMERO
# E SUAS RESPECTIVAS POSIÇÕES.

numero = []

for n in range(0, 5):
    numero.append(int(input(f"Digite um número para a posição {n}: ")))
print('-'*30)
print(f'Os números digitados foram: {numero}')
print('-'*30)
print(f'O maior número da lista é {max(numero)}, que está na(s) posição(ões): ', end='')
for i, v in enumerate(numero):
    if v == max(numero):
        print(i, end=' ')
print(f'\nO menor número da lista é {min(numero)}, que está nas posição(ões): ', end='')
for i, v in enumerate(numero):
    if v == min(numero):
        print(i, end=' ')

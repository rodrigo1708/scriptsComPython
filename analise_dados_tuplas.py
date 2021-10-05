# ANÁLISE DE NÚMEROS DE UMA TUPLA

numero = ()  # Declaração de uma tupla

# Inserindo elementos dentro de uma tupla:

for n in range(0, 4):
    numero += (int(input("Digite um número inteiro: ")), )
print(f'Você digitou os valores {numero}.')  # Mostra na tela os valores digitados pelo usuário.
print(f'O número 9 aparece {numero.count(9)} vezes.')  # Mostra na tela quantas vezes o usuário digitou o número nove.
# Mostrando se o número 3 foi digitado e em que posição o número 3 aparece primeiro
if 3 in numero:
    print(f'O primeiro número 3 foi digitado na {numero.index(3)+1}ª posição.')
else:
    print("O número 3 não foi digitado.")

# Mostrando se existem números pares digitados pelo usuário.

par = False
for p in numero:
    if p % 2 == 0:
        print(p, end=' ')
        par = True
if not par:
    print('Nenhum número par foi digitado.')
else:
    print('foi/foram o(s) número(s) par(es) digitado(s).')

# Criar um programa que leia vários números pelo teclado. No final da execução o programa mostre a média de todos os
# valores digitados, qual o maior e o menor valor. O programa deve perguntar se o usuário quer continuar ou não a
# digitar valores.

c = soma = media = maior = menor = 0
continuar = ''
while continuar != 'N':
    n = int(input("Digite um número qualquer: "))
    continuar = str(input("Deseja digitar mais valores [S/N]? ")).strip().upper()[0]
    soma += n
    c += 1
    if c == 1:  # Com um número digitado (C = 1), o maior e menor número serão iguais ao número digitado.
        maior = menor = n
    else:  # A partir do segundo número digitado, o programa verifica o maior e menor número.
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    while continuar[0] != 'N' and continuar[0] != 'S':
        continuar = str(input("Digite uma opção válida ['S' para sim ou 'N' para não]: ")).strip().upper()[0]
media = soma / c
print("Foram digitados {} números. "
       "A soma desses números é {}. A média dos números digitados é {:.2f}.".format(c, soma, media))
print("O maior número digitado foi {} e o menor número foi {}.".format(maior, menor))

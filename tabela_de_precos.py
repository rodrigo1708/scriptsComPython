# TABELA DE PREÇOS - Criar um programa que leia produtos e seus preços e mostre a tabela com os preços no final

produtos = ()  # Declarando a tupla...
while True:
    # Adicionando os nomes dos produtos e seus respectivos valores à tupla...
    produtos += ((str(input("Digite o nome do produto: ")), float(input("Digite o valor: R$ "))), )
    # Pergunta ao usuário se deseja cadastrar mais produtos
    escolha = str(input("Deseja cadastrar mais produtos (S/N)? ")).strip().upper()[0]
    # Verifica se o usuário digitou S ou N para prosseguir ou parar o programa
    while escolha[0] != 'S' and escolha[0] != 'N':
        # Se o usuário digitar algo diferente de S ou N, o programa pede para digitar corretamente
        escolha = str(input("Escolha inválida. Deseja cadastrar mais produtos (S/N)? ")).strip().upper()[0]
    # Se a escolha for igual a N (não), o programa é finalizado e a tabela de preços mostrada
    if escolha[0] == 'N':
        break
print('-'*40)
print('{:^40}'.format('TABELA DE PREÇOS'))
print('-'*40)
# Imprimindo o nome do produto e o seu valor...
for p, v in produtos:
    print(f'{p:.<33}R$ ', end='')
    print('{:>.2f}'.format(v))
print('-'*40)

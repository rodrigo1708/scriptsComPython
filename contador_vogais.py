# CONTADOR DE VOGAIS - Programa para contar as vogais de uma palavra digitada pelo usuário

palavra = ()  # Incializando a tupla
v = 0  # Criando uma variável para contar as vogais

while True:  # Loop infinito para o usuário digitar a palavra
    palavra += (str(input("Digite uma palavra, nome ou frase (sem acentos): ")), )
    # O usuário decide se quer ou não continuar a digitar mais palavras
    escolha = str(input("Deseja inserir mais palavras? (S/N) ")).strip().upper()[0]
    # O programa verifica se a escolha do usuário coincide com S (sim) ou N (não)
    while escolha[0] != 'S' and escolha[0] != 'N':
        escolha = str(input("Digite uma opção válida. Deseja continuar? (S/N) ")).strip().upper()[0]
    # Se o usuário digitar N (não) o programa sai do loop e inicia a contagem das vogais
    if escolha == 'N':
        break
print('Você digitou as palavras {}.\n'.format(palavra))
# Contando as vogais...
for p in palavra:  # Separando os elementos dentro da tupla
    print(f'\nNa palavra/frase/nome {p} temos as vogais: ', end='')
    for letra in p:  # Separando as letras de cada elemento
        if letra.lower() in 'aeiou':  # Verificando se existe vogal em cada palavra digitada pelo usuário
            v += 1  # Contagem das vogais
            print(letra, end=' ')
    print()
    print(f'Sendo {v} vogais.')
    v = 0  # Reinicia a contagem das vogais para cada elemento da tupla.

# PROGRAMA PARA MOSTRAR UMA MATRIZ 3X3 COM A FORMATAÇÃO CORRETA E ANALISAR OS VALORES INSERIDOS

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # DEFINIÇÃO DE MATRIZ 3X3

for l in range(0, 3):  # LAÇO FOR QUE DETERMINA O NÚMERO DE LINHAS
    for c in range(0, 3):  # LAÇO FOR ANINHADO QUE DETERMINA O NÚMERO DE COLUNAS
        matriz[l][c] = int(input(f'Digite um valor na posição [{l}, {c}]: '))  # PREENCHIMENTO DA MATRIZ LINHA X COLUNA
# ESCREVENDO A MATRIZ 3X3 NA FORMATAÇÃO CORRETA
print('=-'*40)
print('A matriz 3x3 é:')
for linha in matriz:
    for coluna in linha:
        print(f'{coluna:^5}', end='')  # CENTRALIZA OS NÚMEROS DENTRO DA MATRIZ EM UM ESPAÇAMENTO DE 5
    print()  # O PRINT VAZIO PULA UMA LINHA
# A) SOMA DOS VALORES PARES DA MATRIZ
# B) SOMA DOS VALORES DA TERCEIRA COLUNA DA MATRIZ
somapar = somacoluna = 0  # VARIÁVEL PARA SOMAR OS VALORES PARES E OS VALORES DA TERCEIRA COLUNA
for linha in matriz:
    for coluna, valor in enumerate(linha):  # VARRENDO TODOS OS VALORES DA MATRIZ
        if valor % 2 == 0:  # VERIFICANDO SE O VALOR DE CADA ELEMENTO DA MATRIZ É PAR
            somapar += valor
        if coluna == 2:  # DEFININDO A TERCEIRA COLUNA DA MATRIZ PARA SOMAR OS VALORES DESTA COLUNA
            somacoluna += valor
print('=-'*40)
print(f'A soma dos valores pares da matriz é igual a: {somapar}.')
print(f'A soma dos valores da terceira coluna é: {somacoluna}.')
# C) VERIFICANDO O MAIOR VALOR DA SEGUNDA LINHA DA MATRIZ
for linha, valor in enumerate(matriz):
    if linha == 1:  # DEFININDO A SEGUNDA LINHA DA MATRIZ PARA VERIFICAR O VALOR MÁXIMO DESTA LINHA
        print(f'O maior valor digitado na segunda linha da matriz foi: {max(valor)}.')
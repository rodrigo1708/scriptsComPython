# PROGRAMA PARA MOSTRAR UMA MATRIZ 3X3 COM A FORMATAÇÃO CORRETA

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # DEFINIÇÃO DE MATRIZ 3X3

for l in range(0, 3):  # LAÇO FOR QUE DETERMINA O NÚMERO DE LINHAS
    for c in range(0, 3):  # LAÇO FOR ANINHADO QUE DETERMINA O NÚMERO DE COLUNAS
        matriz[l][c] = int(input(f'Digite um valor na posição [{l}, {c}]: '))  # PREENCHIMENTO DA MATRIZ LINHA X COLUNA
# ESCREVENDO A MATRIZ 3X3 NA FORMATAÇÃO CORRETA
for linha in matriz:
    for coluna in linha:
        print(f'{coluna:^5}', end='')  # CENTRALIZA OS NÚMEROS DENTRO DA MATRIZ EM UM ESPAÇAMENTO DE 5
    print()  # O PRINT VAZIO PULA UMA LINHA

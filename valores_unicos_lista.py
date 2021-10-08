# CRIAÇÃO DE PROGRAMA QUE NÃO PERMITE A INCLUSÃO DE VALORES DUPLICADOS EM UMA LISTA

# DECLARANDO A VARIÁVEL DO TIPO LISTA
valores = []

while True:
    n = int(input("Digite outro número inteiro: "))
    # VERIFICANDO SE O VALOR INCLUÍDO JÁ EXISTE DENTRO DA LISTA:
    if n not in valores:  # SE O VALOR NÃO EXISTIR NA LISTA, O NÚMERO É INCLUÍDO
        valores.append(n)
    else:  # SE O VALOR JÁ EXISTIR NA LISTA, O PROGRAMA NÃO INCLUI
        print("Número duplicado. Valor não adicionado!")
    escolha = str(input("Digite S se quiser continuar, ou N se quiser parar o programa: ")).strip().upper()[0]
    while 'S' not in escolha and 'N' not in escolha:
        escolha = str(input("Digite uma opção válida (S para continuar, N para parar o programa): ")).strip().upper()[0]
    if escolha == 'N':
        break
# MOSTRANDO A LISTA DE VALORES ÚNICOS EM ORDEM CRESCENTE
print('-'*25)
print(f'Os valores incluídos, em ordem crescente, foram: {sorted(valores)}')

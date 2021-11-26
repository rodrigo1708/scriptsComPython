from cadastro_pessoas.lib.interface import *
from cadastro_pessoas.lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'

if not arqExiste(arq):
    criarArquivo(arq)
else:
    print('Arquivo encontrado!')

while True:
    sleep(1)
    resposta = menu()
    if resposta == 1:
        lerArquivo(arq)
        sleep(1)
    elif resposta == 2:
        titulo('NOVO CADASTRO')
        sleep(1)
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        sleep(1)
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print(linha())
        print('Saindo programa...')
        sleep(1)
        break

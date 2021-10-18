# CADASTRO DE PESSOAS (DICIONÁRIOS, LISTAS E ESTRUTURAS DE REPETIÇÃO E CONDICIONAIS) 2.0

from time import sleep

cadastro = []  # Lista para armazenar as pessoas cadastradas
dados = {}  # Dicionário para armazenar cada pessoa cadastrada
totidade = media = 0  # Variáveis para o cálculo da média de idade
print('=' * 15, 'CADASTRO DE PESSOAS', '=' * 15)

while True:
    print('-' * 40)
    nome = str(input('Digite o nome: ')).strip().upper()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M/F): ')).strip().upper()[0]
    while 'M' not in sexo and 'F' not in sexo:
        sexo = str(input('Escolha inválida. Seleciona M para masculino ou F para feminino: ')).strip().upper()[0]
    print('=' * 40)
    escolha = str(input('Quer continuar (S/N)? ')).strip().upper()[0]
    while 'N' not in escolha and 'S' not in escolha:
        escolha = str(input('Escolha inválida! Digite "S" para continuar ou "N" '
                            'para encerrar o programa: ')).strip().upper()[0]
    totidade += idade  # Soma das idades inseridas
    dados = {'Nome': nome, 'Idade': idade, 'Sexo': sexo}  # Inclusão das pessoas cadastradas em um dicionário
    cadastro.append(dados)  # Inclusão dos dicionários em uma lista
    if escolha == 'N':
        break
sleep(1)
print('=' * 40)
print(f'Foram cadastradas {len(cadastro)} pessoas.')
sleep(1)
media = totidade / len(cadastro)  # Cálculo da média de idade das pessoas cadastradas
print(f'A média de idade das pessoas cadastradas é de {media:.2f} anos.')
sleep(1)
print('-' * 40)
print('As mulheres cadastradas são:')
sleep(1)
for f in cadastro:  # Lista de mulheres cadastradas no programa
    if f['Sexo'] == 'F':
        print(f['Nome'])
        sleep(1)
print('-' * 40)
print('As pessoas com idade acima da média são: ')
sleep(1)
for m in cadastro:  # Lista de pessoas com idade acima da méda do grupo de pessoas cadastradas
    if m['Idade'] > media:
        print(f'Nome: {m["Nome"]}, Idade: {m["Idade"]} anos.')
        sleep(1)
print('<< FIM DO PROGRAMA >>')

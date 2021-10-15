# BOLETIM DE NOTAS COM LISTAS COMPLEXAS

from time import sleep

dados = []  # Inicializando lista que receberá os nomes dos alunos e as respectivas notas
notas = []  # Lista que armazenará os dados

while True:  # Recebendo os nomes e notas dos alunos
    dados.append(str(input("Digite o nome do aluno: ")).strip().upper())
    for n in range(1, 3):
        dados.append(float(input(f'Digite a {n}ª nota: ')))
    notas.append(dados[:])  # Incluindo os nomes e notas na lista
    dados.clear()
    escolha = str(input("Deseja continuar (S/N)? ")).strip().upper()[0]
    while 'S' not in escolha and 'N' not in escolha:
        escolha = str(input("Escolha inválida! Digite S para continuar ou N para parar: ")).strip().upper()[0]
    if escolha == 'N':
        break
print('=' * 30)
print(f'{"Nº":<4}{"NOME":^10}{"MÉDIA":>8}')
print('=' * 30)
for i, m in enumerate(notas):  # Escrevendo o as médias dos alunos
    media = (m[1] + m[2]) / 2
    numero = i + 1
    print(f'{numero:<4}{m[0]:^10}{media:>8.2f}')
print('=' * 30)
while True:  # Visualizando as notas individuais de cada aluno
    aluno = int(input("Digite o número do aluno para visualizar as notas individualizadas "
                      "(Digite 0 para encerrar o programa): "))
    while aluno > len(notas):
        aluno = int(input("Escolha um número válido, ou 0 para encerrar: "))
        print('-' * 30)
    if aluno == 0:
        print('Encerrando o programa...')
        sleep(1)
        print('-x' * 15)
        print('FIM DO PROGRAMA')
        break
    for i, a in enumerate(notas):
        if aluno == i + 1:
            sleep(1)
            print(f'As notas de {a[0]} são {a[1]} e {a[2]}.')
            print('=' * 30)

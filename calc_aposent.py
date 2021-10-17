# CÁLCULO DE APOSENTADORIA COM DICIONÁRIO

from datetime import date
from time import sleep

pessoa = {'Nome': str(input("Digite o nome: "))}
sexo = str(input("Digite o sexo (M ou F): ").strip().upper()[0])
while 'M' not in sexo and 'S' not in sexo:
    sexo = str(input("Opção inválida. Escolha M para Masculino ou F para Feminino: "))
pessoa['Sexo'] = sexo
nasc = int(input("Digite o ano de nascimento: "))
today = date.today()
pessoa['Idade'] = today.year - nasc
pessoa['CTPS'] = int(input("Digite o número da CTPS (apenas números. Digite 0 se não tiver CTPS): "))
print('=' * 40)
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input("Digite o ano de contratação: "))
    pessoa['Salario'] = float(input("Digite o salário: R$ "))
    print('=' * 40)
    sleep(1)
    pessoa['Aposentadoria'] = (pessoa['Contratação'] - nasc) + 35
    if pessoa['Sexo'] == 'M' and pessoa['Aposentadoria'] < 65:
        pessoa['Aposentadoria'] = nasc + 65
    elif pessoa['Sexo'] == 'F' and pessoa['Aposentadoria'] < 61:
        pessoa['Aposentadoria'] = nasc + 61
    for k, v in pessoa.items():
        print(f'{k}: {v}')
        sleep(1)
else:
    print(f'Nome: {pessoa["Nome"]};'
          f'\nIdade: {pessoa["Idade"]} anos de idade.'
          f'\nNão possui CTPS.')

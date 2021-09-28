# SIMULADOR DE CAIXA ELETRÔNICO

print("="*30)
print("{:^30}".format('Banco RF'))
print("="*30)
print("Notas disponíveis para saque: R$ 100 - R$ 50 - R$ 20 - R$ 10 - R$ 5")
saque = int(input("Qual o valor do saque? R$ "))
# Verificando se o valor do saque é divisível por 5
while saque % 5 != 0 or saque <= 0:
    saque = int(input("Valor para saque indisponível. Digite outro valor para saque: R$ "))
# Cálculo de quantas notas de 100, 50, 20, 10 e 5 reais serão necessárias para o saque
if saque % 5 == 0:
    cedula100 = int(saque / 100)
    resto100 = saque % 100
    if cedula100 != 0:
        print(f"{cedula100} cédulas de R$ 100,00")
    cedula50 = int(resto100 / 50)
    resto50 = resto100 % 50
    if cedula50 != 0:
        print(f"{cedula50} cédulas de R$ 50,00")
    cedula20 = int(resto50 / 20)
    resto20 = resto50 % 20
    if cedula20 != 0:
        print(f"{cedula20} cédulas de R$ 20,00")
    cedula10 = int(resto20 / 10)
    resto10 = resto20 % 10
    if cedula10 != 0:
        print(f"{cedula10} cédulas de R$ 10,00")
    cedula5 = int(resto10 / 5)
    resto5 = resto10 % 5
    if cedula5 != 0:
        print(f"{cedula5} cédulas de R$ 5,00")

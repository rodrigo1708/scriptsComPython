# PROGRAMA DE CADASTRO DE PESSOAS (ESTRUTURAS DE REPETIÇÃO E ESTRUTURAS CONDICIONAIS)

# Contador de quantidades
qtdidade = masc = qtdf20 = 0
while True:
    print("-"*10, "CADASTRE UMA PESSOA", "-"*10)
    idade = int(input("Idade: "))
    # Enquanto a idade digitada for 0 ou menor que 0, o programa não avança
    while idade <= 0:
        idade = int(input("Digite uma idade válida: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    # Enquanto o sexo digitado não for M ou F, o programa não avança
    while sexo[0] not in 'MF':
        sexo = str(input("Digite uma opção sexual válida: ")).strip().upper()[0]
    # Condições para a contagem das quantidades para análise
    if idade >= 18:
        qtdidade += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        qtdf20 += 1
    continuar = str(input("Quer cadastrar mais pessoas [S/N]? ")).strip().upper()[0]
    # Enquanto não for digitado S ou N para continuar ou parar, o programa não avança
    while continuar[0] not in 'SN':
        continuar = str(input("Digite uma opção válida (S para SIM ou N para NÃO): ")).strip().upper()[0]
    # Caso seja digitado N, o programa se encerra e sai do loop
    if continuar == 'N':
        break
print("="*35)
print(f"Total de pessoas maiores de 18 anos: {qtdidade}.\nAo todo temos {masc} homens cadastrados."
      f"\nTemos {qtdf20} mulheres com menos de 20 anos.")
print("="*35)



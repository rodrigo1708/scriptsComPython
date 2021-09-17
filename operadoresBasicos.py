from time import sleep
valor1 = float(input("Digite o primeiro número: "))
valor2 = float(input("Digite o segundo número: "))
escolha = 0
while escolha != 6:
    print('''Opções: 
            [ 1 ] - SOMAR;
            [ 2 ] - MULTIPLICAR;
            [ 3 ] - SUBTRAIR;
            [ 4 ] - DIVIDIR;
            [ 5 ] - ESCOLHER NOVOS NÚMEROS;
            [ 6 ] - SAIR DO PROGRAMA.''')
    escolha = int(input("Escolha uma opção: "))
    while escolha >= 7:
        escolha = int(input("Escolha uma opção válida: "))
    if escolha == 1:
        resultado = valor1 + valor2
        print("A soma entre {} e {} é igual a {:.2f}.".format(valor1, valor2, resultado))
        print("="*40)
        sleep(1)
    elif escolha == 2:
        resultado = valor1 * valor2
        print("A multiplicação entre {} e {} é igual a {:.2f}.".format(valor1, valor2, resultado))
        print("=" * 40)
        sleep(1)
    elif escolha == 3:
        resultado = valor1 - valor2
        print("A subtração entre {} e {} é igual a {:.2f}.".format(valor1, valor2, resultado))
        print("=" * 40)
        sleep(1)
    elif escolha == 4:
        resultado = valor1 / valor2
        print("A divisão entre {} e {} é igual a {:.2f}.".format(valor1, valor2, resultado))
        print("=" * 40)
        sleep(1)
    elif escolha == 5:
        print("Digite os novos números:")
        valor1 = float(input("Primeiro valor: "))
        valor2 = float(input("Segundo valor: "))
print("Finalizando o programa...")
print("="*40)
sleep(2)
print("Fim do programa. Volte sempre!")
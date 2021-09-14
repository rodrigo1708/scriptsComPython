def palindromo():
    print('--'*13)
    print("Verificador de Palíndromo!")
    print('--'*13)
    nome = str(input("Digite uma frase ou palavra qualquer: ")).strip().lower()
    nome = nome.split()
    nome = ''.join(nome)
    if nome[::-1] == nome:
        print("A frase/palavra é um palíndromo!")
    else:
        print("A frase/palavra não é palíndromo.")


        # VERIFICADOR DE PALÍNDROMO UTILIZANDO A ESTRUTURA FOR
def palindromo2():
    print('\n')
    print('--'*13)
    print("Verificador de Palíndromo!")
    print('--'*13)
    nome = str(input("Digite uma frase ou palavra qualquer: ")).strip().lower()
    sep = nome.split()
    junto = ''.join(sep)
    inverso = ''
    for letra in range(len(junto) - 1, -1, -1):
        inverso += junto[letra]
    if inverso == junto:
        print("A palavra/frase é um palíndromo!")
    else:
        print("A palavra/frase não é palíndromo.")


palindromo()
palindromo2()
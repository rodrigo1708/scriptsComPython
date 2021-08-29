def imc():
    altura = float(input("Digite a sua altura: "))
    peso = float(input("Digite seu peso: "))
    imc = peso / (altura ** 2)

    print("Seu IMC é {:.1f}. Seu status é: ".format(imc), end=" ")
    if imc < 18.5:
        print("Abaixo do peso.")
    elif imc <= 25:
        print("Peso ideal.")
    elif imc <= 30:
        print("Sobrepeso.")
    elif imc <= 40:
        print("Obesidade.")
    else:
        print("Obesidade mórbida.")


imc()

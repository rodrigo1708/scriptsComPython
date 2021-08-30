from datetime import date


def categoria():
    nasc = int(input("Digite o ano de nascimento do atleta: "))
    anoAtual = date.today().year
    idade = anoAtual - nasc
    if idade <= 9:
        print("O atleta tem {} anos de idade. Sua categoria é MIRIM.".format(idade))
    elif idade <= 14:
        print("O atleta tem {} anos de idade. Sua categoria é INFANTIL.".format(idade))
    elif idade <= 19:
        print("O atleta tem {} anos de idade. Sua categoria é JÚNIOR.".format(idade))
    elif idade <= 25:
        print("O atleta tem {} anos de idade. Sua categoria é SÊNIOR.".format(idade))
    else:
        print("O atleta tem {} anos de idade. Sua categoria é MASTER".format(idade))


categoria()

        # VERIFICADOR DE MAIOR E MENOR PESO
def peso():
    kg = []
    for c in range(1, 6):
        kg.append(float(input("Digite o peso da {}ª pessoa: ".format(c))))
    print("O maior peso lido foi {} Kg.\nO menor peso lido foi {} Kg.".format(max(kg), min(kg)))


peso()

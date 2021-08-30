print("-----"*12)
print("Saiba se três segmentos de reta podem formar um triângulo!!")
print("-----"*12)
l1 = float(input("Digite o primeiro segmento: "))
l2 = float(input("Digite o segundo segmento: "))
l3 = float(input("Digite o terceiro segmento: "))

if (l2 - l3) < l1 < (l2 + l3) and (l1 - l3) < l2 < (l1 + l3) and (l1 - l2) < l3 < (l1 + l2):
    print("Os segmentos de reta de medida {}, {} e {} podem formar um triângulo! O triângulo é do tipo:".format(l1, l2, l3))
    if l1 == l2 == l3:
        print("Equilátero.")
    elif l1 != l2 != l3 != l1:
        print("Escaleno.")
    else:
        print("Isósceles.")
else:
    print("Os segmentos de reta não podem formar um triângulo!")

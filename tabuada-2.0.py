n = mult = 0
while True:
    print("-" * 40)
    n = int(input("Qual tabuada você quer visualizar? "))
    print("-"*40)
    if n < 0:
        print("PROGRAMA TABUADA ENCERRADO!")
        break
    for c in range(1, 11):
        mult = n * c
        print(f"{n} x {c} = {mult}")

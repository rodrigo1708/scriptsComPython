# Programa para escrever os 10 primeiros termos de uma progressão aritmética

n1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
n10 = n1 + (10 - 1) * razao

for c in range(n1, n10 + razao, razao):
    print(c, end="-> ")
print("Fim.")

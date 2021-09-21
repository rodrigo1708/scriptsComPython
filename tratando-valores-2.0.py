# Programa para ler vários números inteiros digitados pelo usuário. O programa deve parar quando o número 999 for
# digitado e no final, o programa deve mostrar a soma dos números digitados e quantos números foram inseridos
# excluindo o 999 da soma final e da contagem de números inseridos no programa.

soma = n = c = 0
while True:
    n = float(input("Digite um valor [digite 999 para parar]: "))
    if n == 999:
        break
    c += 1
    soma += n
print(f"Você digitou {c} números e a soma entre eles foi {soma}.")

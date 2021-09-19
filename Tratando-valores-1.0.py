# Programa para ler vários números inteiros digitados pelo usuário. O programa deve parar quando o número 999 for
# digitado e no final, o programa deve mostrar a soma dos números digitados e quantos números foram inseridos
# excluindo o 999 da soma final e da contagem de números inseridos no programa.

soma = n = c = 0
# Variável SOMA = Realiza a soma dos números digitados
# Variável C = Contador para verificar quantos números foram digitados
while n != 999:
    n = int(input("Digite um valor [digite 999 para parar]: "))
    soma += n  # Soma os números digitados
    c += 1  # Conta quantos números foram digitados
if n == 999:
    soma -= 999
    c -= 1
print("Você digitou {} números e a soma entre eles foi {}.".format(c, soma))

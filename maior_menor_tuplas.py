from random import randint

numero = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print("Os valores sorteados foram: ", end='')
for n in numero:
    print(n, end=' ')
print(f'\nO menor número da lista é: {min(numero)}.\n')
print(f'O maior número da lista é: {max(numero)}.')

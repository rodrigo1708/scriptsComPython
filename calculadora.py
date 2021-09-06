class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def divisao(self):
        return round((self.a / self.b), 3)

    def multiplicacao(self):
        return self.a * self.b


if __name__ == '__main__':
    num = [int(input("Digite 'a': ")), int(input("Digite 'b': "))]
    calc = Calculadora(num[0], num[1])
    print("a = ", calc.a)
    print("b = ", calc.b)
    print("Soma = ", calc.soma())
    print("Subtração = ", calc.subtracao())
    print("Divisão = ", calc.divisao())
    print("Multiplicação = ", calc.multiplicacao())


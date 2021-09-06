class Televisao:
    def __init__(self):
        # Televisão desligada
        self.ligada = False
        # Canal inicial da televisão
        self.canal = 5

    def power(self):
        # Confere se a televisão está ligada ao pressionar o botão "power"
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1


if __name__ == '__main__':
    tv = Televisao()
    # APERTA BOTÃO POWER (LIGA A TV)
    tv.power()
    print("A tv está ligada? {}".format(tv.ligada))
    tv.power()
    # APERTA BOTÃO POWER (DESLIGA A TV)
    print("A tv está ligada? {}".format(tv.ligada))
    # LIGA A TV
    tv.power()
    print("A tv está ligada? {}".format(tv.ligada))
    # CANAL INICIAL
    print("Canal: {}".format(tv.canal))
    # AUMENTA CANAL
    tv.aumenta_canal()
    tv.aumenta_canal()
    print("Aumenta 02 canais. Canal: {}".format(tv.canal))
    # DIMINUI CANAL
    tv.diminui_canal()
    tv.diminui_canal()
    tv.diminui_canal()
    print("Diminui 03 canais. Canal: {}".format(tv.canal))

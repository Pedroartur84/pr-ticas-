class carro:
    def __init__(self):
        self.motor_ligado = 0

    def ligar_motor(self):
        self.motor_ligado = True
        print("motor ligado")

    def desligar_motor(self):
        self.motor_ligado = False
        print("motor desligado")

vermelho = carro()
vermelho.ligar_motor()
vermelho.desligar_motor()
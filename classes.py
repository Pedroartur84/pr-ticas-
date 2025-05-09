class Gato:
    def miar(self):
        print("Miau!")


class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.1416 * self.raio ** 2

    def calcular_circunferencia(self):
        return 2 * 3.1416 * self.raio


class Carro:
    def __init__(self):
        self.motor_ligado = False

    def ligar_motor(self):
        self.motor_ligado = True
        print("Motor ligado.")

    def desligar_motor(self):
        self.motor_ligado = False
        print("Motor desligado.")


class Cachorro:
    def latir(self):
        print("Au au!")


class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado.")
        else:
            print("Saldo insuficiente.")


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
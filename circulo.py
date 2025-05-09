class circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.1416 * self.raio ** 2
    
    def calcular_circuferencia(self):
        return 2 * 3.1416 * self.raio
    
bola = circulo(raio=100)

area = bola.calcular_area()

circuferencia = bola.calcular_circuferencia()

print(f"a area é {area} e a circunferençia é {circuferencia}")
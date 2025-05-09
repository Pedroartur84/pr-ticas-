class triangulo:
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return(self.base * self.altura) / 2
        
retangulo1 = triangulo(base=10, altura=30)
area = retangulo1.calcular_area()

print(f"a area é {area}")

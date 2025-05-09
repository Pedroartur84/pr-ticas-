class retangulo:
    def __init__(self, largura, altura):
        self.lagura = largura
        self.altura = altura

    def calcular_area(self):
        return self.lagura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.lagura + self.altura)
    
retangulo1 = retangulo(largura=100, altura=50)
area = retangulo1.calcular_area()
perimetro = retangulo1.calcular_perimetro()

print(f"a area é {area}")
print(f"o perimetro é {perimetro}")
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

# Criando os nós manualmente
no1 = No('A')
no2 = No('B')
no3 = No('C')

# Encadeando os nós
no1.proximo = no2
no2.proximo = no3

# Percorrendo a lista e contando os nós
contador = 0
atual = no1

while atual:
    contador += 1
    atual = atual.proximo

# Mostrando o resultado
print(f"Quantidade de elementos: {contador}")
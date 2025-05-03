def verificar_sinal(numero):
    if numero > 0:
        return 'p'
    else:
        return 'n'
    
valor = float(input("digite um numero: "))

resultado = verificar_sinal(valor)
print(f"O resulatado é {resultado}")
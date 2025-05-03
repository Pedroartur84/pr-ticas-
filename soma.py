def somar(n1,n2,n3):
    resultado = n1 + n2 + n3
    return {
        "resultado":resultado
    }

parametros = list(map(float, input("digite tres parametros: ").split()))

resultado = somar(*parametros)

print(f"a soma é {resultado ['resultado']}") 
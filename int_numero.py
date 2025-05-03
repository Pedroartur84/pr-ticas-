def contar_digitos(numero):
    return len(str(abs(numero)))

while True:
    try:
        entrada = input("Digite um número inteiro (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            break
        numero = int(entrada)
        print(f"O número {numero} possui {contar_digitos(numero)} dígitos.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
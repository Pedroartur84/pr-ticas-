# ==== Módulo: Jogo da Adivinhação ====
import random

def gerar_numero_secreto():
    return random.randint(1, 100)

def receber_chute():
    return int(input("Digite seu chute (1 a 100): "))

def verificar_chute(chute, segredo):
    if chute == segredo:
        return "Acertou!"
    elif chute < segredo:
        return "Muito baixo!"
    else:
        return "Muito alto!"

def iniciar_jogo_adivinhacao():
    segredo = gerar_numero_secreto()
    tentativas = 0
    while True:
        chute = receber_chute()
        tentativas += 1
        resultado = verificar_chute(chute, segredo)
        print(resultado)
        if resultado == "Acertou!":
            break
    print(f"Você acertou em {tentativas} tentativas!")

def jogar_adivinhacao():
    print("Bem-vindo ao Jogo da Adivinhação!")
    iniciar_jogo_adivinhacao()
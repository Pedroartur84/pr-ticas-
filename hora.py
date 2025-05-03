def converter_horario(hora24, minuto24):
    """Converte horário de 24h para 12h e retorna o período (A/P)"""
    if hora24 < 0 or hora24 > 23 or minuto24 < 0 or minuto24 > 59:
        return None, None
    
    if hora24 == 0:
        return 12, 'A'  # Meia-noite
    elif 1 <= hora24 < 12:
        return hora24, 'A'  # Manhã
    elif hora24 == 12:
        return 12, 'P'  # Meio-dia
    else:
        return hora24 - 12, 'P'  # Tarde/noite

def exibir_horario(hora12, minuto12, periodo):
    """Exibe o horário no formato 12h com AM/PM"""
    if hora12 is None or periodo is None:
        print("Horário inválido!")
    else:
        periodo_extenso = "A.M." if periodo == 'A' else "P.M."
        print(f"{hora12}:{minuto12:02d} {periodo_extenso}")

def main():
    while True:
        print("\nConversor de Horário (24h → 12h)")
        try:
            hora = int(input("Digite a hora (0-23): "))
            minuto = int(input("Digite os minutos (0-59): "))
            
            hora12, periodo = converter_horario(hora, minuto)
            exibir_horario(hora12, minuto, periodo)
            
        except ValueError:
            print("Por favor, digite números inteiros válidos.")
        
        repetir = input("\nDeseja converter outro horário? (s/n): ").lower()
        if repetir != 's':
            break

if __name__ == "__main__":
    main()
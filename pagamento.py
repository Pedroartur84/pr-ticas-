def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso <= 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03  # 3% de multa
        juros = valor_prestacao * (0.001 * dias_atraso)  # 0.1% por dia de atraso
        return valor_prestacao + multa + juros

def main():
    relatorio = {
        'quantidade': 0,
        'valor_total': 0.0
    }
    
    print("Sistema de Cálculo de Prestações (digite 0 para encerrar)")
    
    while True:
        try:
            valor = float(input("\nDigite o valor da prestação: R$ "))
            if valor == 0:
                break
            
            dias = int(input("Digite o número de dias em atraso: "))
            
            if valor < 0 or dias < 0:
                print("Valores não podem ser negativos. Tente novamente.")
                continue
            
            valor_pago = valorPagamento(valor, dias)
            relatorio['quantidade'] += 1
            relatorio['valor_total'] += valor_pago
            
            print(f"Valor a ser pago: R$ {valor_pago:.2f}")
            
        except ValueError:
            print("Entrada inválida. Digite valores numéricos.")
    
    # Exibe relatório
    print("\n--- Relatório do Dia ---")
    print(f"Quantidade de prestações pagas: {relatorio['quantidade']}")
    print(f"Valor total recebido: R$ {relatorio['valor_total']:.2f}")

if __name__ == "__main__":
    main()
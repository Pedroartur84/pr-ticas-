def calcular_gasto_combustivel(consumo_km_por_litro, distancia_percorrida, valor_litro_combustivel):
    litros_gastos = distancia_percorrida / consumo_km_por_litro

    custo_total = litros_gastos * valor_litro_combustivel

    return {
        "litros_gastos": litros_gastos,
        "custo_total": custo_total
    }

consumo = 12  
distancia = 300  
valor_litro = 5.50  

resultado = calcular_gasto_combustivel(consumo, distancia, valor_litro)

print(f"Litros gastos: {resultado['litros_gastos']:.2f}")
print(f"Custo total: R${resultado['custo_total']:.2f}")
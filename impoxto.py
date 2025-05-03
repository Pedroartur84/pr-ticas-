def SomaInposto(TaxaImposto,Custo):
    custo_com_inposto = Custo + (Custo * TaxaImposto / 100)
    return custo_com_inposto

taxa = int(input("digite a taxa: "))
valor = int(input("digite o valor: "))

new_valor = SomaInposto(taxa,valor)

print(f"O custo com inposto é {new_valor}")
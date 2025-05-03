def convertor(litros):
    milimetro = litros * 1000

    return milimetro

player_litros = float(input("Quantos litros voçe quer converter?"))
litros = convertor(player_litros)

print(f"{player_litros} litros equivalem a {litros} milimetros.")
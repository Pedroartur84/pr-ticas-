def convertor(dolar):
    real = dolar * 5.65

    return real

player_litros = float(input("Quantos dolas voçe quer converter?"))
real = convertor(player_litros)

print(f"{player_litros} dolares equivalem a {real} reais.")
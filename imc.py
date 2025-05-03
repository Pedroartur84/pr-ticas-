def calcular_imc_e_classificar(peso, altura):

  imc = peso / (altura ** 2)

  if imc < 18.5:
    classificacao = "Magro"
  elif 18.5 <= imc < 24.9:
    classificacao = "Normal"
  elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
  elif 30 <= imc < 34.9:
    classificacao = "Obeso (Grau 1)"
  elif 35 <= imc < 39.9:
    classificacao = "Obeso (Grau 2)"
  else:
    classificacao = "Obeso Mórbido (Grau 3)"

  return f"IMC: {imc:.2f} - Classificação: {classificacao}"

peso = float(input("Digite seu peso em quilos: "))
altura = float(input("Digite sua altura em metros: "))

resultado = calcular_imc_e_classificar(peso, altura)
print(resultado)
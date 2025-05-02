def calcular_media_e_situacao(notas):

  media = sum(notas) / len(notas)

  if media >= 7:
    situacao = "Aprovado"
  elif media >= 6:
    situacao = "recuperação"
  else:
    situacao = "Reprovado"

  return {"media": media, "situacao": situacao}

# .splint = divide a string por espaços, nesse casso
# map(float,...) = converte cada item para float, nesse casso
# list(...) trasforma o resultado em uma lista
notas_aluno = list(map(float, input("digite suas notas separadas por espaços: ").split()))

resultado = calcular_media_e_situacao(notas_aluno)

# Acessa media do dicionario resultado que recebe a função calcular_media_e_situacao
print(f"Média: {resultado['media']}")
# Acessa situação do dicionario resultado que recebe a função calcular_media_e_situacao
print(f"Situação: {resultado['situacao']}")
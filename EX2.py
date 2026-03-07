# Peça ao usuário:
# - Número atual de seguidores
# - Quantosseguidores ele ganha por dia
# - Quantos dias ele quer simular
# Calcule:
# - Quantosseguidores ele terá ao final do período
# - Quantos seguidores ele ganhou no total
# Mostre:
# - Total de seguidores após o período
# - Total de seguidores ganhos

numatual= int(input("Digite quantos seguidores voce tem atualmente: "))
quantseguidorespordia = int(input("Digite quantos seguidores voce ganha por dia: "))
quantDias = int(input("Digite quantos dias voce quer simular: "))
quantseguidoresnofinal = quantseguidorespordia* quantDias
quantseguidorestotais = quantseguidoresnofinal + numatual





print("\n------------------------------------------\n")


print("Total de seguidores após o período:", quantseguidorestotais)
print("Total de seguidores ganhos:", quantseguidoresnofinal)

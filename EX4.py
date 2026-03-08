# Peça ao usuário:
# - Valor da mesada-
# - Quanto ele pretende guardar-
# - Quanto ele gasta com lanches-
# - Quanto ele gasta com jogos ou lazer-
# Calcule:
# - Total de gastos
# - Quanto sobra ou falta no final do mês
# Mostre:
# - Total gasto-
# - Valor restante (ou valor que faltou, se for negativo)-


valordamesada = int(input("Digite o valor da mesada: "))
quantelepretendeguardar = int(input("Digite quanto ele pretende guardar: "))
quantgastacomlanches= int(input("Digite quanto ele gasta com lanches: "))
quantgastacomjogosoulazer = int(input("Digite quanto ele gasta com jogs ou lazer: "))


totaldegastos = quantgastacomjogosoulazer + quantgastacomlanches
valorrestante = totaldegastos - quantelepretendeguardar



print("\n------------------------------------------\n")




print("Total gasto:", totaldegastos)
print("Valor restante:", valorrestante)
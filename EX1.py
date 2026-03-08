# string = 'oi'
# int = 2
# float = 2.3
# quantVitorias = input("Digite quantas vezes voce ganhou: ")
# quantVitorias = int(quantVitorias)



# Mostre:
# - Total de partidas
# - Pontuação final
# - Percentual de vitórias



quantVitorias = int(input("Digite quantas vezes voce ganhou: "))
quantDerrotas = int(input("Digite quantas vezes voce perdeu: "))
quantpontosporVitorias = int(input("Digite quantos pontos vale cada vitória: "))
partJogadas = quantDerrotas + quantVitorias
pontConquis = quantpontosporVitorias * quantVitorias

# total = 10
# vitorias = 3

# 1 - 10 = 10
# 2 - 100 * 3 = 300
# 3 - 300 / 10 = 30
 

percVitorias = (quantVitorias*100) / partJogadas





print("\n------------------------------------------\n")




# print("Vitorias:", quantVitorias)
# print("Derotas:", quantDerrotas)
# print("Pontos por vitoria:", quantpontosporVitorias)
print("Pontos:", pontConquis)
print("Patidas jogadas:", partJogadas)
print("Percentual de Vitorias:", percVitorias, '%')


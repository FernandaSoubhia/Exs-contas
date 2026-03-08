# Peça ao usuário:
# - Número de jogos disputados
# - Total de gols marcados
# - Total de assistências
# Calcule:
# - Média de gols por jogo
# - Média de participações em gol por jogo (gols + assistências)
# Mostre:
# - Média de gols por jogo
# - Média de participações por jogo




numjogosdisputaods= int(input("Digite o numero de jogos disputados: "))
totaldegolsmar = int(input("Digite o total de gols marcados: "))
totalassistencias = int(input("Digite o total de assistencias: "))

# Leitura dos números
n1 = float(input("Digite a quantidade de gols da primeria partidade: "))
n2 = float(input("Digite a quantidade de gols da segunda partidade: "))
n3 = float(input("Digite a quantidade de gols da terceira partidade: "))
n4 = float(input("Digite a quantidade de gols da quarta partidade: "))
# Cálculo da média
media = (n1 + n2 + n3 + n4) / 4

medpartidegolporjogo = (totaldegolsmar + totalassistencias) *4 /2

print("\n------------------------------------------\n")

print("A média é de gols :", media)
print("Participaçoes por jogo:", medpartidegolporjogo)
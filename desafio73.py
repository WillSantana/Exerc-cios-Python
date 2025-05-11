# Desafio 073 – Tuplas com Times de Futebol: 
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre: 
# A) apenas os 5 primeiros colocados; 
# B) os últimos 4 colocados da tabela; 
# C) uma lista com os times em ordem alfabética; 
# D) em que posição na tabela está o time da Cruzeiro.​


times = (
    "Flamengo",
    "Palmeiras",
    "Bragantino",
    "Cruzeiro",
    "Fluminense",
    "Internacional",
    "Bahia",
    "São Paulo",
    "Botafogo",
    "Ceará",
    "Vasco",
    "Corinthians",
    "Juventude",
    "Mirassol",
    "Fortaleza",
    "Vitória",
    "Atlético-MG",
    "Grêmio",
    "Santos",
    "Sport"
)

print ('-=-' * 20)
print("Os 5 primeiros colocados são:", times[:5])
print('-=-' * 20)
print("Os 4 últimos colocados são:", times[-4:])
print('-=-' * 20)
print("Times em ordem alfabética:", sorted(times))
print('-=-' * 20)
print("O Cruzeiro está na posição:", times.index("Cruzeiro") + 1)
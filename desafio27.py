# Programa para ler o nome completo de uma pessoa e mostrar o primeiro e o último nome separadamente

# Solicita o nome completo do usuário
nome_completo = input("Digite seu nome completo: ").strip()

# Divide o nome completo em uma lista de nomes
nomes = nome_completo.split()

# Obtém o primeiro e o último nome
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

# Exibe o primeiro e o último nome
print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
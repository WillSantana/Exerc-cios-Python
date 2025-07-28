# Solicita ao usuário que insira um número entre 0 e 9999
numero = input("Digite um número entre 0 e 9999: ")

# Preenche o número com zeros à esquerda para garantir que tenha 4 dígitos
numero = numero.zfill(4)

# Exibe cada dígito separadamente
print(f"Unidade: {numero[3]}")
print(f"Dezena: {numero[2]}")
print(f"Centena: {numero[1]}")
print(f"Milhar: {numero[0]}")
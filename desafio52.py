# 52 - Números Primos: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.​

# Solicita um número ao usuário
numero = int(input("Digite um número inteiro: "))
total = 0  # Inicializa o contador de divisores
# Loop para verificar os divisores do número
for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end='')  # Cor amarela
        total += 1  # Incrementa o contador de divisores
    else:
        print('\033[31m', end='') # Cor vermelha
    print(f"{i}", end=' ')  # Exibe o divisor
print('\033[m')  # Reseta a cor
# Verifica se o número é primo

# Exibe o divisor
print(f"número {numero} foi divisível {total} vezes ")

if total == 2:
    print(f"O número {numero} é primo.")  # Mensagem se o número for primo
else:
    print(f"O número {numero} não é primo.")

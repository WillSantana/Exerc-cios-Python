# Desafio 082 – Separando Valores em Listas Diferentes
# Crie um programa que leia vários números e os armazene em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares 
# e os valores ímpares digitados, respectivamente.

numeros = []
n = int(input('Digite um número (ou -1 para sair): '))
while n != -1:
    # Verifica se o número já existe na lista
    if n not in numeros:
        numeros.append(n)
    else:
        print('Número já existe na lista. Não será adicionado.')
    n = int(input('Digite um número (ou -1 para sair): '))
    
print('-' * 60)    
# Exibe a quantidade de números digitados
print(f'Você digitou {len(numeros)} números.')
print('-' * 60)
numeros_pares = [valor for valor in numeros if valor % 2 == 0]
if numeros_pares:
    print(f"Os números pares digitados foram: {numeros_pares}")
else:
    print("Nenhum número par foi digitado.")
numeros_impares = [valor for valor in numeros if valor % 2 != 0]
if numeros_impares:
    print(f"Os números ímpares digitados foram: {numeros_impares}")
else:
    print("Nenhum número ímpar foi digitado.")
print('-' * 60)
print('Fim do programa.')
print('-' * 60)
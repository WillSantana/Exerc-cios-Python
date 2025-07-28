# Desafio 081 – Extraindo Dados de uma Lista
#Crie um programa que leia vários números e os armazene em uma lista. No final, mostre:
    #Quantos números foram digitados
    #A lista de valores, ordenada de forma decrescente
    #Se o valor 5 foi digitado e está ou não na lista
    
numeros = []

while True:
    valor = int(input('Digite um número (ou -1 para sair): '))
    if valor == -1:
        break
    # Verifica se o valor já existe na lista
    if valor not in numeros:
        numeros.append(valor)
    else:
        print('Valor já existe na lista. Nâo será adicionado.')
    # Adiciona o valor à lista
    print(f'Valor {valor} adicionado á lista. ')
    print('-' * 40)
# Exibe a quantidade de números digitados
print(f'Você digitou {len(numeros)} números.')
# Exibe a lista de valores em ordem decrescente
numeros.sort(reverse=True)
print(f'A lista de valores em ordem decrescente é: {numeros}')
# Verifica se o valor 5 foi digitado e está na lista
if 5 in numeros:
    print('O valor 5 foi digitado e está na lista.')
else:
    print('O valor 5 não foi digitado ou não está na lista.')
print('-' * 40)
print('Fim do programa.')
print('-' * 40)
    
    
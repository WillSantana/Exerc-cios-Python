# Desafio 084 – Lista Composta e Análise de Dados.
# Crie um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
# No final, mostre:
    # Quantas pessoas foram cadastradas
    # Uma listagem com as pessoas mais pesadas
    # Uma listagem com as pessoas mais leves
    
nome = []
peso = []

# Loop para receber os dados do usuário
while True:
    nome.append(str(input('Digite o nome: ')))
    peso.append(float(input('Digite o peso: ')))
    
    # Verifica se o usuário deseja continuar
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    elif continuar != 'S':
        print('Opção inválida. Tente novamente.')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('-' * 40)
    
# Exibe a quantidade de pessoas cadastradas
print(f'Foram cadastradas {len(nome)} pessoas.')

# Exibe a lista de pessoas mais pesadas
peso_maximo = max(peso)
print(f'O maior peso foi {peso_maximo} kg. ', end='')
for i in range(len(nome)):
    if peso[i] == peso_maximo:
        print(f'As pessoas mais pesadas foram: {nome[i]} com {peso[i]} kg.')
        
# Exibe a lista de pessoas mais leves
peso_minimo = min(peso)
print(f'O menor peso foi {peso_minimo} kg. ', end='')
for i in range(len(nome)):
    if peso[i] == peso_minimo:
        print(f'As pessoas mais leves foram: {nome[i]} com {peso[i]} kg.')
print('-' * 40)
print('Fim do programa.')
print('-' * 40)

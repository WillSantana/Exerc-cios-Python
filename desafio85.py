# Desafio 085 – Listas com Pares e Ímpares
# Crie um programa onde o usuário possa digitar sete valores numéricos 
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

pares = []
impares = []

# Loop para receber 7 valores do usuário
for i in range(7):
    valor = int(input(f'Digite o {i+1}º valor: '))
    
    # Verifica se o valor é par ou ímpar e adciona à lista correspondente
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    
    # Ordena as listas
    pares.sort()
    impares.sort()
    
    # Exibe os resultados
print('-' * 60)
print('Analisando os valores digitados...')
print('-' * 60)
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')
print('-' * 60)
print('Fim do programa.')
    
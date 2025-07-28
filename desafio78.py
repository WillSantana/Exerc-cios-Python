# Desafio 078 – Maior e Menor Valores na Lista
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# lista = []
valores = []

# Adiciona 5 valores à lista
for i in range(5):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    valores.append(valor)
    
# Encontra o maior e menor valor e suas posições
maior = max(valores)
menor = min(valores)
posicao_maior = valores.index(maior)

# Exibe os resultados
print('-' * 40)
print('Analisando os valores digitados...')
print('-' * 40)
print(f'O maior valor digitado foi {maior} na posição {posicao_maior}.')
print(f'O menor valor digitado foi {menor} na posição {valores.index(menor)}.')
print(f'A lista completa é: {valores}')


#forrma de fazer do professor
# lista = []
# maior = 0
# menor = 0
# for i in range(0, 5):
#   lista.append(int(input(f'Digite o {i + 1}º valor: ')))
#   if i == 0:
#     maior = menor = lista[i]
#   else:
#     if lista[i] > maior:
#       maior = lista[i]
#     if lista[i] < menor:
#       menor = lista[i]
#print('-' * 40)
#print('Analisando os valores digitados...')
#print('-' * 40)
#print(f'Voce digitou os valores {lista}')
#print(f'O maior valor digitado foi {maior} nas posições ', end='')
# for i, v in enumerate(lista):
#   if v == maior:
#     print(f'{i}...', end='')
#print(f'O menor valor digitado foi {menor} nas posições ', end='')
# for i, v in enumerate(lista):
#   if v == menor:
#     print(f'{i}...', end='')
#print(f'A lista completa é: {lista}')
# print('-' * 40)
# print('Fim do programa.')
# print('-' * 40)
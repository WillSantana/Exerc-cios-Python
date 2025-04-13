# 55 - Maior e Menor da Sequência: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.​

maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f"Digite o peso da {1}ª pessoa: "))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso lido foi: {maior} kg")
print(f"O menor peso lido foi: {menor} kg")

# funçao def maior_menor_peso():

# Exemplo de maior e menor peso
# def maior_menor_peso():
#     pesos = []  # Lista para armazenar os pesos
#     for i in range(1, 7): # Loop para ler os pesos
#         peso = float(input(f"Digite o peso da {i}ª pessoa: "))  # Lê o peso
#         pesos.append(peso)  # Adiciona o peso à lista
#     maior_menor_peso = max(pesos) # Encontra o maior peso
#     menor_peso = min(pesos) # Encontra o menor peso
#     return maior_menor_peso, menor_peso # Retorna os pesos
# maior_peso, menor_peso = maior_menor_peso() # Chama a função e armazena os resultados
# print(f"O maior peso lido foi: {maior_peso} kg") # Exibe o maior peso
# print(f"O menor peso lido foi: {menor_peso} kg") # Exibe o menor peso
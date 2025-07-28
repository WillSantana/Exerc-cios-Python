# Desafio 064 – Tratando Vários Valores v1.0
# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos números foram 
# digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
contador = 0
print("Seja bem-vindo ao programa de soma de números!")
print('=-=' * 15)
numero = int(input("Digite um número inteiro (999 para sair): "))
while numero != 999:
    soma += numero
    contador +=1
    numero = int(input("Digite um número inteiro (999 para sair): "))
print('=-=' * 15)
print(f"Você digitou {contador} números e a soma entre eles foi {soma}.")


# # Exemplo de sequência de Fibonacci usando a estrutura while True
# while True:
#     numero = int(input("Digite um número inteiro (999 para parar): "))
#     if numero == 999:
#         break
#     soma += numero
#     contador += 1

# print(f"Você digitou {contador} números e a soma entre eles foi {soma}.")
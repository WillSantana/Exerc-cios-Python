# Desafio 066 – Vários Números com Flag: 
# Crie um programa que leia números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos números foram 
# digitados e qual foi a soma entre eles (desconsiderando o flag).​


soma = 0
cont = 0

while True: # Loop infinito para continuar pedindo números
    num = int(input("Digite um número inteiro (ou 999 para sair): "))
    if num == 999: # Condição de parada
        break
    cont += 1 # Incrementa o contador
    soma += num # Soma os números digitados
print(f"Você digitou {cont} números e a soma entre eles foi {soma}.") 


# While True avançado
# while True: # Loop infinito para continuar pedindo números
#     try:
#         num = int(input("Digite um número inteiro (ou 999 para sair): "))
#         if num == 999: # Condição de parada
#             break 
#         if 'contador' not in locals():  # Verifica se 'contador' não existe
#             contador = 0
#         contador += 1
#         if 'soma' not in locals():  # Verifica se 'soma' não existe
#             soma = 0
#         soma += num
#     except ValueError:  # Tratamento de erro para entrada inválida
#         print("Entrada inválida. Por favor, digite um número inteiro.")
#     except Exception as e:  # Tratamento de erro inesperado
#         print(f"Erro inesperado: {e}")
# print(f"Você digitou {contador} números e a soma entre eles foi {soma}.")



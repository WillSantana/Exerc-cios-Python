# Desafio 065 – Maior e Menor Valores: Crie um programa que leia vários 
# números inteiros pelo teclado. No final da execução, mostre a média entre 
# todos os valores e qual foi o maior e o menor valores lidos.​

maior = 0
menor = 0
soma = 0
contador = 0
media = 0
resposta = 'S'
print("=-=" * 15)
print("Seja bem-vindo ao programa de soma de números!")
print("Digite 999 para sair.")
print('=-=' * 15)
while resposta in 'Ss':
        numero = int(input("Digite um número inteiro: "))
        soma += numero
        contador += 1
        
        if contador == 1: # Verifica se é o primeiro número
            maior = menor = numero # Inicializa maior e menor com o primeiro número
        else:
            if numero > maior: # Verifica se o número atual é maior
                maior = numero
            if numero < menor: # Verifica se o número atual é menor
                menor = numero
        resposta = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
        
media = soma / contador if contador > 0 else 0 # Calcula a média     
print('=-=' * 15)
print(f"Você digitou {contador} números e a soma entre eles foi {soma}.")
print(f"O maior número digitado foi {maior} e o menor número digitado foi {menor}.")
print(f"A média dos números digitados é {media}.")




# # Exemplo de maior e menor peso em while True
# while True:
#     try:
#         num = int(input("Digite um número inteiro (ou 0 para sair): "))
#         if num == 0:
#             break
#         if 'maior' not in locals() or num > maior: # Verifica se 'maior' não existe ou se o número atual é maior
#             maior = num
#         if 'menor' not in locals() or num < menor: # Verifica se 'menor' não existe ou se o número atual é menor
#             menor = num
#         if 'contador' not in locals():
#             contador = 0
#         contador += 1
#         if 'soma' not in locals():
#             soma = 0
#         soma += num 
#     except ValueError:
#         print("Entrada inválida. Por favor, digite um número inteiro.")
#     except Exception as e:  
#         print(f"Erro inesperado: {e}")
#     finally:
#         print("Fim do programa.")
        

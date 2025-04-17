# Desafio 065 – Maior e Menor Valores: Crie um programa que leia vários 
# números inteiros pelo teclado. No final da execução, mostre a média entre 
# todos os valores e qual foi o maior e o menor valores lidos.​

# # Exemplo de maior e menor peso em while

while True:
    try:
        num = int(input("Digite um número inteiro (ou 0 para sair): "))
        if num == 0:
            break
        if 'maior' not in locals() or num > maior: # Verifica se 'maior' não existe ou se o número atual é maior
            maior = num
        if 'menor' not in locals() or num < menor: # Verifica se 'menor' não existe ou se o número atual é menor
            menor = num
        if 'contador' not in locals():
            contador = 0
        contador += 1
        if 'soma' not in locals():
            soma = 0
        soma += num 
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
    except Exception as e:  
        print(f"Erro inesperado: {e}")
    finally:
        print("Fim do programa.")
        

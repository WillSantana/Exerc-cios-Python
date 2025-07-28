# Desafio 063 – Sequência de Fibonacci v1.0: Escreva um programa que leia 
# um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma 
# Sequência de Fibonacci.​

numero = int(input("Digite um número inteiro para calcular os primeiros termos da sequências de Fibonacci: "))
if numero < 0:
    print("Número inválido. O número deve ser maior ou igual a zero.")
else:
    fib = [0,1] # Inicializa a lista com os dois primeiros termos
    while len(fib) < numero:
        fib.append(fib[-1] + fib[-2]) #
    # Calcula o próximo termo
    print(f"Os primeiros {numero} termos da sequência de Fibonacci são: {fib[:numero]}") # Exibe os termos




# # Exemplo de sequência de Fibonacci usando a estrutura função
# def fibonacci(n):
#     fib = [0, 1] # Inicializa a lista com os dois primeiros termos
#     for i in range(2, n):
#         fib.append(fib[i-1] + fib[i-2])  # Calcula o próximo termo
#     return fib[:n]  # Retorna os primeiros n termos

# Usando a estrutura while True
# Exemplo de sequência de Fibonacci
# while True:
#     try:
#         n = int(input("Digite um número inteiro para calcular os primeiros termos da sequências de Fibonacci (ou -1 para sair): "))
#         if n == -1:
#             print("Saindo do programa...")
#             break
#         elif n < 0:
#             print("Número inválido. O número deve ser maior ou igual a zero.")
#         else:
#             fib = [0, 1] # Inicializa a lista com os dois primeiros termos
#             for i in range(2, n):
#                 fib.append(fib[i-1] + fib[i-2]) # Calcula o próximo termo
#             print(f"Os primeiros {n} termos da sequência de fibonacci são: {fib[:n]}") # Exibe os termos
#     except ValueError:
#         print("Entrada inválida. Por favor, digite um número inteiro.")
#      except Exception as e:
#          print(f"Erro inesperado: {e}")
#      finally:
# print("Fim do programa.")            
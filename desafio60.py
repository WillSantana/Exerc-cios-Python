# Desafio 060 – Cálculo do Fatorial: 
# Faça um programa que leia um número qualquer e mostre 
# o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120.​


from time import sleep
numero = int(input("Digite um número inteiro para calcular o fatorial: "))
contador = numero # Inicializa o contador com o número digitado
fatorial = 1 # Inicializa o fatorial com 1
print(f"Calculando o fatorial de {numero}...") # Mensagem de início
while numero > 0:
    fatorial *= numero # Multiplica o fatorial pelo número atual
    numero -= 1 # Decrementa o número
    if numero > 0: # Se o número ainda for maior que 0
        print(f"{numero + 1} x ", end="") # Exibe o número atual seguido de "x"
    else: # Se o número for 0
        print(f"{numero + 1} = ", end="") # Exibe o número atual seguido de "="
        sleep(2) # Pausa de 1 segundo
        print(fatorial) # Exibe o resultado final







# Exemplo usando biblioteca math
# from math import factorial
# numero = int(input("Digite um número inteiro para calcular o fatorial: "))
# fatorial = (numero)
# print(f"O fatorial de {numero} é {fatorial}.")



# Exemplo de cálculo de fatorial usando while True
#  while True:
#     try:
#         n = int(input("Digite um número inteiro para calcular o fatorial (ou -1 para sair): "))
#         if n == -1:
#             print("Saindo do programa...")
#             break
#         elif n < 0:
#             print("Número inválido. O fatorial não é definido para números negativos.")
#         else:
#             fatorial = 1
#             movimento = []  # Lista para armazenar os números do cálculo
#             for i in range(n, 0, -1):  # Loop de n até 1
#                 fatorial *= i
#                 movimento.append(str(i))  # Adiciona o número à lista como string
#             print(f"{n}! = {' x '.join(movimento)} = {fatorial}")
#     except ValueError:
#         print("Entrada inválida. Por favor, digite um número inteiro.")
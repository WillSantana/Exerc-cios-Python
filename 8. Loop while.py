# contador = 0
# while contador < 11:
#     print(contador)
#     contador += 1

# #<<<<<<<<<<<<<<<<<<<<<<<<

# cont = 0                                             
# print ( "iniciando a contagem. Digite 'sair' a qualquer momento para parar.")
# while True:
#     print (f"Contador:{cont}")                       
#     entrada = input("Pressione Enter para continuar ou 'Sair':")
#     if entrada.lower() == 'sair':
#         break                                           
#     cont += 1

# #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# import random

# numero_secreto = random.randint(1, 10)
# tentativas = 0

# print("Bem-vindo ao jogo 'Adivinhe o Número Secreto'!")
# print("Eu pensei em um número entre 1 e 10. Tente adivinhar!")
# print("Se quiser desistir, digite 'sair'.")

# while True:
#     try:
#         entrada = input("Qual é o seu palpite? (ou 'sair'): ").lower()
#         if entrada == 'sair':
#             print("Entendido. Você desistiu. O número secreto era:", numero_secreto)
#             break     
#         palpite = int(entrada)
#         tentativas += 1
#         if palpite < numero_secreto:
#             print("Muito baixo! Tente um número maior.")
#         elif palpite > numero_secreto:
#             print("Muito alto! Tente um número menor.")
#         else:
#             print(f"Parabéns! Você acertou o número secreto ({numero_secreto}) em {tentativas} tentativas!")
#             break
#     except ValueError:
#         print("Entrada inválida. Por favor, digite um número ou 'sair'.")
#     except Exception as e: 
#         print(f"Ocorreu um erro inesperado: {e}")
#         break
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

import random
aleatorio = random.randint(1, 10)

print("Bem-vindo ao jogo 'Adivinhe o Número Secreto'!")
print("Eu pensei em um número entre 1 e 10. Tente adivinhar!")
print("Se quiser desistir, digite 'sair'.")

tentativas = 0
while True:
    try:
        entrada = input("Qaul é o seu palpite? (ou 'sair'): ").lower()
        if entrada == 'sair':
            print("Entendido. Você desistiu. O número secreto era:", aleatorio)
        break
        palpite = int(entrada)
        tentativas += 1
        if palpite < aleatorio:
            print("muito baixo! Tente um numero maior.")
        elif palpite > aleatorio:
            print("Muito alto! Tente um numero menor.")
        else:
            print(f"Parabéns! Voce acertou o numero secreto ({aleatorio}) em {tentativas} tentativas!")
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um numero ou sair.")
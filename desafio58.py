# Desafio 058 – Jogo da Adivinhação v2.0: 
# Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.​


from random import randint  # Importa a biblioteca random para gerar números aleatórios
from time import sleep # Importa a biblioteca time para usar a função sleep

computador = randint(0, 10) # O computador escolhe um número aleatório entre 0 e 10
tentativas = 0 # Inicializa o contador de tentativas
print("=-=" * 20) # Imprime uma linha de separação
print("Vou pensar em um número entre 0 e 10. Tente adivinhar!") # Mensagem inicial
print('Sera que você consegue adivinhar qual foi?') # Mensagem de incentivo
print("=-=" * 20) # Imprime outra linha de separação

acertou = False # Inicializa a variável acertou como False
while not acertou: # Loop infinito até o jogador acertar
    jogador = int(input("Qual é o seu palpite? ")) # Lê o palpite do jogador
    tentativas += 1 # Incrementa o contador de tentativas
    print("PROCESSANDO...") # Mensagem de processamento
    sleep(2) # Pausa o programa por 2 segundos
    if jogador < computador: # Verifica se o palpite é menor que o número do computador
        print("Mais... Tente mais uma vez.") # Mensagem de dica
    elif jogador > computador: # Verifica se o palpite é maior que o número do computador
        print("Menos... Tente mais uma vez.") # Mensagem de dica
    else: # Se o palpite for igual ao número do computador
        acertou = True # O jogador acertou
        
        print(f"Parabéns! Você acertou o número {computador} em {tentativas} tentativas.") # Mensagem de sucesso    
        print("=-=" * 20) # Imprime outra linha de separação
        print("Fim do jogo!") # Mensagem de fim de jogo


# jogo de advinhação usando função

# from random import randint  # Importa a biblioteca random para gerar números aleatórios
# from time import sleep  # Importa a biblioteca time para usar a função sleep

# def jogo_adivinhacao():
#     while True:  # Loop para permitir que o jogador jogue novamente
#         print("=-=" * 20)  # Imprime uma linha de separação
#         print("Vou pensar em um número entre 0 e 10. Tente adivinhar!")  # Mensagem inicial
#         print("=-=" * 20)  # Imprime outra linha de separação
        
#         numero = randint(0, 10)  # O computador escolhe um número aleatório entre 0 e 10
#         tentativas = 0  # Inicializa o contador de tentativas
        
#         while True:  # Loop infinito até o jogador acertar
#             try:
#                 palpite = int(input("Qual é o seu palpite? "))  # Lê o palpite do jogador
#                 tentativas += 1  # Incrementa o contador de tentativas
#                 print("PROCESSANDO...")
#                 sleep(2)
#                 if palpite < numero:
#                     print("Mais... Tente mais uma vez.")
#                 elif palpite > numero:
#                     print("Menos... Tente mais uma vez.")
#                 else:
#                     print(f"Parabéns! Você acertou o número {numero} em {tentativas} tentativas.")
#                     break
#             except ValueError:
#                 print("Por favor, insira um número válido.")
        
#         print("=-=" * 20)
#         print("Fim do jogo!")  # Mensagem de fim de jogo
#         print("=-=" * 20)  # Imprime outra linha de separação
        
#         # Pergunta ao jogador se deseja jogar novamente
#         jogar_novamente = input("Deseja jogar novamente? (S/N): ").strip().upper()
#         if jogar_novamente != 'S':
#             print("Obrigado por jogar! Até a próxima.")
#             break

# # Chama a função para iniciar o jogo
# jogo_adivinhacao()
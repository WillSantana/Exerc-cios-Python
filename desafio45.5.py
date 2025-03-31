import random
import time

# Opções do jogo
opcoes = ['Pedra', 'Papel', 'Tesoura']

# Exibe as opções para o jogador
print("Suas opções:")
print("[0] Pedra")
print("[1] Papel")
print("[2] Tesoura")

# Entrada do jogador
jogador = int(input("Qual é a sua jogada? "))

# Valida a entrada do jogador
if jogador < 0 or jogador > 2:
    print("Jogada inválida!")
else:
    # Escolha do computador
    computador = random.randint(0, 2)

    # Exibe as escolhas
    print("\nJO")
    time.sleep(0.5)
    print("KEN")
    time.sleep(0.5)
    print("PÔ!!!\n")
    print(f"Computador jogou: {opcoes[computador]}")
    print(f"Jogador jogou: {opcoes[jogador]}")

    # Determina o vencedor
    if computador == jogador:
        print("Empate!")
    elif (jogador == 0 and computador == 2) or \
         (jogador == 1 and computador == 0) or \
         (jogador == 2 and computador == 1):
        print("Você venceu!")
    else:
        print("Computador venceu!")
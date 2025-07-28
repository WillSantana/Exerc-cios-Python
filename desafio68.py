# Desafio 068 – Jogo do Par ou Ímpar: 
# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# biblioteca random para gerar números aleatórios e time para fazer pausas no programa
import random
import time
print('Vamos jogar Par ou Ímpar!')
print('-' * 20)
vitoria = 0

# Loop infinito para continuar jogando até perder o jogador escolhe um número inteiro e o computador gera um número aleatório
while True:
    jogador = int(input('Digite um número inteiro: '))
    computador = random.randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        print('=-' * 20)
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} ', end='')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    print('-' * 20)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria +=1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria +=1
        else:
            print('Você PERDEU!')
            break
print(f'Você venceu {vitoria} vezes consecutivas.')
print('=-' * 20)
print('Fim do programa!')
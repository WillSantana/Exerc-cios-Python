import random
a = random.randint(1, 3) # Escolha do computador
print('Vamos jogar Jokenpô!')
print('Escolha uma opção:')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
jogador = int(input('Digite a opção: '))
if jogador == 1:
    print('Você escolheu Pedra!')
elif jogador == 2:
    print('Você escolheu Papel!')
else:
    print('Você escolheu Tesoura!')
if a == 1:
    print('O computador escolheu Pedra!')
elif a == 2:
    print('O computador escolheu Papel!')
else:
    print('O computador escolheu Tesoura!')
if jogador == 1 and a == 3:
    print('Você ganhou!')
elif jogador == 2 and a == 1:
    print('Você ganhou!')
elif jogador == 3 and a == 2:
    print('Você ganhou!')
elif jogador == a:
    print('Empate!')
else:
    print('Você perdeu!')
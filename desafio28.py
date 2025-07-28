print('-=-' * 15 )
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 15 )
import random
n = int(input('Digite um número inteiro de 0 a 5: '))
print('Processando...')
r = random.randint(0, 5) # Gera um número aleatório de 0 a 5
if n == r:
    print('Parabéns! Você acertou!, o número sorteado foi {}!'.format(r))
else:
    print(f'Você errou! O número sorteado foi {r}!')
print('Fim do programa')

















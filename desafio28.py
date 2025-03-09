import random
n = int(input('Digite um número inteiro de 0 a 5: '))
r = random.randint(0, 5) # Gera um número aleatório de 0 a 5
if n == r:
    print('Parabéns! Você acertou!')
else:
    print(f'Você errou! O número sorteado foi {r}!')
print('Fim do programa')
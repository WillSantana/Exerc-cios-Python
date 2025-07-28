from math import sin, cos, tan, radians
# sin(x): Retorna o seno de x, em radianos.
# cos(x): Retorna o cosseno de x, em radianos.
# tan(x): Retorna a tangente de x, em radianos.
# radians(x): Converte x de graus para radianos.
Angulo = float(input('Digite o valor do ângulo: '))
print(f'O valor do Seno é {sin(radians(Angulo)):.2f}')
print(f'O valor do Cosseno é {cos(radians(Angulo)):.2f}')
print(f'O valor da Tangente é {tan(radians(Angulo)):.2f}')


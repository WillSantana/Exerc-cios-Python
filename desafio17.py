from math import hypot
cto = float(input('Digite o valor do Cateto Oposto: '))
cta = float(input('Digite o valor do Cateto Adjacente: '))
# hypot(x, y): Retorna a raiz quadrada da soma dos quadrados dos argumentos
hta = hypot(cto, cta)
print(f'O valor da Hipotenusa é {hta:.2f}')
#42 - Analisando triângulos v2.0: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: – EQUILÁTERO: todos os lados iguais; – ISÓSCELES: dois lados iguais, um diferente; – ESCALENO: todos os lados diferentes.
comprimento1 = float(input('Digite o comprimento da primeira reta: '))
comprimento2 = float(input('Digite o comprimento da segunda reta: '))
comprimento3 = float(input('Digite o comprimento da terceira reta: '))
if comprimento1 < comprimento2 + comprimento3 and comprimento2 < comprimento1 + comprimento3 and comprimento3 < comprimento1 + comprimento2:
    if comprimento1 == comprimento2 == comprimento3:
        print('As retas podem formar um triângulo \033[32mEQUILÁTERO!\033[m')
    elif comprimento1 == comprimento2 or comprimento1 == comprimento3 or comprimento2 == comprimento3:
        print('As retas podem formar um triângulo \033[35mISÓSCELES!\033[m')
    else:
        print('As retas podem formar um triângulo \033[34mSCALENO!\033[m')
else:
    print('\033[32mAs retas não podem formar um triângulo!\033[m')

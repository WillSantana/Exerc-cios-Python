comprimento1 = float(input('Digite o comprimento da primeira reta: '))
comprimento2 = float(input('Digite o comprimento da segunda reta: '))
comprimento3 = float(input('Digite o comprimento da terceira reta: '))
if comprimento1 < comprimento2 + comprimento3 and comprimento2 < comprimento1 + comprimento3 and comprimento3 < comprimento1 + comprimento2:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')    
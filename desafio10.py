v = float(input('Digite o valor que voce tem na carteira: R$ '))
d = v / 3.27
d1 = v / 5.83
e = v / 6.07
print(f'Com R${v:.2f} voce pode comprar U$ {d:.2f} dolares da cotação antiga')
print(f'Com R${v:.2f} voce pode comprar U$ {d1:.2f} dolares da cotação atual')
print(f'Com R${v:.2f} voce pode comprar EUR {e:.2f} euros')